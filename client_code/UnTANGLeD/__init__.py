from ._anvil_designer import UnTANGLeDTemplate
from anvil import *


class UnTANGLeD(UnTANGLeDTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
