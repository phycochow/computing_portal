from ._anvil_designer import HomeTemplate
from anvil import *
from anvil.js.window import jQuery

class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        self.column_panel_1.role = 'text-image-row'
