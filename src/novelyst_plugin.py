"""Plugin template for novelyst.

Adds an 'Example' entry to the 'Tools' menu to open a submenu.
The 'Say Hello' command in this submenu opens a message box.

equires Python 3.6+
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_plugin
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import tkinter as tk
from tkinter import messagebox

APPLICATION = 'Example plugin'

# Initialize localization.
LOCALE_PATH = f'{os.path.dirname(sys.argv[0])}/locale/'
try:
    CURRENT_LANGUAGE = locale.getlocale()[0][:2]
except:
    # Fallback for old Windows versions.
    CURRENT_LANGUAGE = locale.getdefaultlocale()[0][:2]
try:
    t = gettext.translation('novelyst_plugin', LOCALE_PATH, languages=[CURRENT_LANGUAGE])
    _ = t.gettext
except:

    def _(message):
        return message


class Plugin:
    """Example plugin class.
    
    Public methods:
        disable_menu() -- disable menu entries when no project is open.
        enable_menu() -- enable menu entries when a project is open.
        on_close() -- Actions to be performed when a project is closed.       
        on_quit() -- Actions to be performed when novelyst is closed.               
    """
    VERSION = '@release'
    NOVELYST_API = '4.28'
    DESCRIPTION = 'Example plugin'
    URL = 'https://peter88213.github.io/novelyst_plugin'

    def install(self, ui):
        """Add a submenu to the 'Tools' menu.
        
        Positional arguments:
            ui -- reference to the NovelystTk instance of the application.
        """
        self._ui = ui

        # Create a submenu
        self._pluginMenu = tk.Menu(self._ui.toolsMenu, tearoff=0)
        self._ui.toolsMenu.add_cascade(label=APPLICATION, menu=self._pluginMenu)
        self._ui.toolsMenu.entryconfig(APPLICATION, state='disabled')
        self._pluginMenu.add_command(label='Say Hello', underline=0, command=self._hello)

    def disable_menu(self):
        """Disable menu entries when no project is open."""
        self._ui.toolsMenu.entryconfig(APPLICATION, state='disabled')

    def enable_menu(self):
        """Enable menu entries when a project is open."""
        self._ui.toolsMenu.entryconfig(APPLICATION, state='normal')

    def on_close(self, event=None):
        """Actions to be performed when a project is closed."""
        pass

    def on_quit(self, event=None):
        """Actions to be performed when novelyst is closed."""
        pass

    def _hello(self):
        message = 'Hello, world!'
        messagebox.showinfo(APPLICATION, message)
