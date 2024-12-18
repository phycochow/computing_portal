from ._anvil_designer import NewsTemplate
from anvil import *
import anvil.server


class News(NewsTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # Home TopNavgBar theme
        if self.base.activated_theme == 'Home':
            self.navg_toggle = (False, False, False, False, False)
        else:
            self.navg_toggle = (True, True, True, True, True)
            
        self.navg_text = ('', '', '', '', '')

        # Any code you write here will run before the form opens.
