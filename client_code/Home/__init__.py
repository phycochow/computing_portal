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
        text = self.rich_text_2
        
        self.grid_panel_1.row = 'gp-centered'
        self.grid_panel_1.clear()
        self.grid_panel_1.add_component(text, row='row_panel', col_xs=0, width_xs=6)
        self.grid_panel_1.add_component(Image(source='_/theme/PalpantLogo.jpeg',
                                              display_mode='fill_width', 
                                              margin=('15px', '0px', '0px', '0px')), # Top, Right, Bottom, Left
                                        row='row_panel',
                                        col_xs=8.5,
                                        width_xs=3.5)


        
        