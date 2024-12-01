from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home

class Base(BaseTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.link_1.text = 'Palpant Group'
        self.link_2.text = 'TRIAGE'

        self.content_panel.add_component(Home())

        # Any code you write here will run before the form opens.
