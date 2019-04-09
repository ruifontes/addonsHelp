#-*- coding:utf-8 -*-
# Copyright (C) 2019 Rui Fontes <rui.fontes@tiflotecnia.com>, Zougane, Rémy and Abdel
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
import os
import addonHandler
import gui
import wx
import globalVars
_curAddon = addonHandler.getCodeAddon()
_addonSummary = _curAddon.manifest['summary']

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
		# Creation of a self.helpMenu object that will point to the NVDA Help menu and create our own submenu, _addonSummary.
		self.hlpMenu = gui.mainFrame.sysTrayIcon.helpMenu
		menu = wx.Menu()
		self.addonHelpMenu = self.hlpMenu.AppendSubMenu(menu, "{arg0}".format(arg0 = _addonSummary))
		# Filter only those addons that have help documentation.
		addonsList = [item for item in addonHandler.getAvailableAddons() if item.getDocFilePath()]
		# If our list contains any elements.
		if len(addonsList) > 0:
			# Add our items in loop in our new submenu, each one with the name of the corresponding addon.
			for item in addonsList:
				newSubMenu = menu.Append(wx.ID_ANY, item.manifest["summary"])
				# Associate the events in each menu item with the self.onOpenHelp function.
				gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, lambda event, args=item: self.onOpenHelp(event, args), newSubMenu)

	def terminate(self):
		# This terminate function is necessary when creating new menus.
		try:
			self.helpMenu.RemoveItem(self.addonHelpMenu)
		except wx.PyDeadObjectError:
			pass

	def onOpenHelp(self, evt, item):
		# This is the function that will handle the events of our submenus.
		# Opens the help of our addon.
		os.startfile(item.getDocFilePath())
