from ._anvil_designer import EpiCopsTemplate
from anvil import *
import anvil.server

class EpiCops(EpiCopsTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # CMPortal TopNavgBar theme
        self.navg_toggle = (True, True, True, True, True)
        self.navg_text = ('About', 'Visuals', 'Predictions', 'Clustering', 'Store')
        
        fig1 = anvil.server.call('create_plots')
        self.image_1.source = fig1
        # Any code you write here will run before the form opens.
