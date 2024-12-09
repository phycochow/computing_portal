from ._anvil_designer import EpiCopsTemplate
from anvil import *
import anvil.server


class EpiCops(EpiCopsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        fig1 = anvil.server.call('create_plots')
    
        self.image_1.source = fig1
        # Any code you write here will run before the form opens.
