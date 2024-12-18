from ._anvil_designer import HomeTemplate
from anvil import *
from anvil.js.window import jQuery
import anvil.js.window

class Home(HomeTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # This is preset, but we can set change_content() to TopNavgUpdate=False if not Home theme
        self.navg_toggle = (False, False, False, False, False)
        self.navg_text = ('', '', '', '', '')
        
        # Any code you write here will run before the form opens.
        
        