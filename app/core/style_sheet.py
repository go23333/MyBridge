# coding: utf-8

from enum import Enum


from qfluentwidgets import StyleSheetBase,Theme,isDarkTheme,qconfig



class StyleSheet(StyleSheetBase,Enum):
    HOME_INTERFACE = "home_interface"
    IMPORT_INTERFACE = "import_interface"
    SETTING_INTERFACE = "setting_interface"
    
    def path(self,theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":/MyBridge/qss/{theme.value.lower()}/{self.value}.qss"