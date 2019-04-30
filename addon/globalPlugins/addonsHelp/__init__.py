# -*- coding: utf-8 -*-
# Copyright (C) 2019 Rui Fontes <rui.fontes@tiflotecnia.com>, Zougane, Remy and Abdel
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
import inputCore
import addonHandler
import gui
import wx
import webbrowser

# For translation
addonHandler.initTranslation()

# Creation of a GlobalPlugin class, derived from globalPluginHandler.GlobalPlugin.
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Creating the constructor of the newly created GlobalPlugin class.
	def __init__(self, *args, **kwargs):
		# Call of the constructor of the parent class.
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		# Creation of our submenu.
		self.createSubMenu()

	def createSubMenu(self):
		# Creation of a self.hlpMenu object that will point to the NVDA Help menu and create our own submenu
		self.hlpMenu = gui.mainFrame.sysTrayIcon.helpMenu
		menu = wx.Menu()
		#. Translators: Label of our first sub-menu.
		self.addonHelpSubMenu = self.hlpMenu.AppendSubMenu(menu, _("Running add-ons &documentation"))
		# Filter only those addons that have help documentation.
		addonsList = [item for item in addonHandler.getAvailableAddons() if item.getDocFilePath() and not item.isDisabled]
		# Add the sub-menu that will list the descriptions of the scripts contained in our add-ons.
		addonsCommands = menu.Append(wx.ID_ANY,
		#. Translators: Label of the sub-menu to view the commands descriptions of the installed add-ons.
		_("Add-ons &commands"),
		#. Translators: Displays the description of the commands contained in each installed add-on.
		_("Description of the scripts contained in each add-on"))
		# Associate a event to this menu 
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, lambda event: self.onOpenDoc(event), addonsCommands)

		# Add our items in loop in our new submenu, each one with the name of the corresponding addon.
		for item in addonsList:
			newSubMenu = menu.Append(wx.ID_ANY, "&" + item.manifest["summary"])
			# Associate the events in each menu item with the self.onOpenHelp function.
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, lambda event, args=item: self.onOpenHelp(event, args), newSubMenu)

		# Filter only those addons that have help documentation.
		disabledAddonsList = [item1 for item1 in addonHandler.getAvailableAddons() if item1.getDocFilePath() and item1.isDisabled]
		# If our list contains any elements.
		if len(disabledAddonsList) > 0:

			# Creation of a self.hlpMenu object that will point to the NVDA Help menu and create our own second submenu
			self.hlpMenu = gui.mainFrame.sysTrayIcon.helpMenu
			menu = wx.Menu()
			#. Translators: Label of our second sub-menu.
			self.disabledAddonHelpSubMenu = self.hlpMenu.AppendSubMenu(menu, _("Disabled add-o&ns documentation"))

			# Add our items in loop in our new submenu, each one with the name of the corresponding addon.
			for item1 in disabledAddonsList:
				newSubMenu1 = menu.Append(wx.ID_ANY, "&" + item1.manifest["summary"])
				# Associate the events in each menu item with the self.onOpenHelp function.
				gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, lambda event, args=item1: self.onOpenHelp(event, args), newSubMenu1)

	def adjustGesture (self, identifier):
		"""
		This method corrects the gestures provided as parameter, inspired from the NVDA core (module gui/settingsDialog.py, class InputGesturesDialog, method _formatGesture).
		"""
		try:
			source, main = inputCore.getDisplayTextForGestureIdentifier(identifier)
			return _("{main} ({source})").format(main=main, source=source)
		except LookupError:
			return identifier

	def updateAddonDic (self, addonDic):
		"""
		This method makes it possible to create a dictionary grouping all the add-ons that contain scripts associated or not with gestures.
		"""
		import addonHandler
		# We gather all the gestures available in a dictionary, thanks to inputCore.manager.getAllGestureMappings.
		allGest = inputCore.manager.getAllGestureMappings(obj=gui.mainFrame.prevFocus, ancestors=gui.mainFrame.prevFocusAncestors)
		# We store the list of installed add-ons in a variable named addonsList.
		addonsList = [ addon for addon in addonHandler.getAvailableAddons ()]
		# We Iterates through the dictionary containing all the available gestures.
		for category in allGest:
			# We create a local variable, storing the value of each of the main items in our dictionary.
			command = allGest[category]
			# These items represent the different categories available.
			# The values retrieved by allGest[category], in turn comprise another dictionary grouping the description of each of the scripts in each category.
			# We Iterates among the dictionary objects for each of the categories.
			for doc in command:
			# Each item of its sub-dictionaries represents the documentation of each of the scripts, which is why it was preferably named doc.
			# We now create a local variable script, which will retrieve each of the values of our sub-dictionary.
					script = command[doc]
					# each of its values is an instance of the inputCore.AllGesturesScriptInfo class for each of the scripts.
					# It's an object representing a script, which is why it was preferably named script.
					# We check if our script is that of an add-on, we will make further checks below.
					if script.moduleName.startswith("globalPlugins") or script.moduleName.startswith("appModules"):
						# The moduleName property of each of these script objects returns the name of the module that contains the script.
						# Now, it's going to be a bit complicated.
						# We point to the script object directly in the appModule or globalPlugin, to check its path.
						scriptMod = getattr (script.cls, "script_{scriptName}".format (scriptName=script.scriptName), None)
						if scriptMod:
							# Here is the path to the module, it will be interesting, because it's it that will reveal if it's an add-on or not.
							modPath = scriptMod.im_func.func_code.co_filename
							# This is the only way we have to retrieve the name of the add-on.
							# We check the presence of the "addons" directory in the path.
							if any (addon.path in modPath for addon in addonsList):
								# There is no longer any doubt, it's an add-on.
								# We get the summary of the add-on.
								addonSum = [addon.manifest["summary"] for addon in addonsList if addon.path in modPath][0]
								# We check the gesture (s) of our script.
								if len (script.gestures) > 0:
									gestInfo = " | ".join ([self.adjustGesture (x) for x in script.gestures])
								else:
									#. Translators: Message to inform there are no command assigned.
									gestInfo = _("Not assigned to gesture or part of layered commands")
								# We try to update our dictionary addonDic, according to whether it has taken knowledge of each item or not.
								try:
									addonDic[addonSum][gestInfo]=script.displayName
								except KeyError:
									# It has not yet read it, so we create the very first sub-dictionary representing each of our scripts contained in each of our add-ons.
									addonDic[addonSum]={}
									# We can now make our update.
									addonDic[addonSum][gestInfo]=script.displayName

	def terminate(self):
		# This terminate function is necessary when creating new menus.
		try:
			if wx.version().startswith("4"):
				self.hlpMenu.Remove(self.addonHelpMenu)
			else:
				self.hlpMenu.RemoveItem(self.addonHelpMenu)
		except:
			pass

	def onOpenHelp(self, evt, item):
		# This is the function that will handle the events of our submenus.
		# Opens the help of our addon on default browser.
		webbrowser.open(item.getDocFilePath())

	def onOpenDoc (self, evt):
		# This is the function that will handle the events of "add-ons commands"submenu. 
		import ui
		addonDic = {}
		self.updateAddonDic (addonDic)
		#. Translators: Name of the list.
		message = u"<h1>{title}</h1><br>".format(title=_("List of commands for running add-ons"))
		for addon in sorted(addonDic, key = lambda item: item.lower()):
			message += u"<h2>{addonSum}</h2>\n<table>\n<tr><th>".format(addonSum=addon)
			#. Translators: The title of the column containing the documentation of each of the scripts.
			message += _("Documentation")
			message += "</th><th>"
			#. Translators: The title of the column containing the command of each of the scripts.
			message += _("Gesture")
			message += "</th></tr>\n"
			script = addonDic[addon]
			for gesture in sorted(script):
				message += u"<tr><td>{doc}</td><td>{gesture}</td></tr>\n".format (doc = script[gesture], gesture=gesture)
			message += "</table>\n"
		ui.browseableMessage (message,
		#. Translators: Title of the HTML message.
		_("Add-ons documentation"),
		True)
