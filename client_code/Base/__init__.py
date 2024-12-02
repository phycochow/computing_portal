from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home

class Base(BaseTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        # self.pages_dict = {'Home' : Home()}
        
        self.link_1.text = 'Palpant Group'
        self.button_1.text = 'TRIAGE'
        self.button_2.text = 'TRIAGE'
        
        # self.content_panel.add_component(self.pages_dict['Home'])
        self.content_panel.add_component(Home())
        
        

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(TRIAGE())

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(EpiCops())

    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(CMPortal())

    def button_4_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(UnTANGLeD())
