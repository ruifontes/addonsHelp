# -*- coding: utf-8 -*-
# Copyright (C) 2019 Rui Fontes <rui.fontes@tiflotecnia.com>, Zougane, Remy and Abdel
# This file is covered by the GNU General Public License.

import addonHandler
import gui
import wx
addonHandler.initTranslation()

def onInstall():
	addon = [x for x in addonHandler.getAvailableAddons() if x.manifest["name"] == "addonsHelp-1.0"]
	if len(addon) > 0:
		addon = addon[0]
		gui.messageBox (
		# Translators: A message informing the user that he has installed an old version that contains a space rather than an underscore.
		_("You have installed the addonsHelp-1.0 add-on which is incompatible with this one. The new name of this add-on is addonsHelp. Click OK to update it."),
		# Translators: The title of the dialogbox.
		_("Update confirmation"),
		wx.OK)
		addon.requestRemove()
