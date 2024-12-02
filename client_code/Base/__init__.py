from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home
from ..TRIAGE import TRIAGE
from ..CMPortal import CMPortal
from ..EpiCops import EpiCops
from ..UnTANGLeD import UnTANGLeD

class Base(BaseTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        # self.pages_dict = {'Home' : Home()}

        self.navg_buttons = [self.button_1, self.button_2, self.button_3, self.button_4]

        # self.content_panel.add_component(self.pages_dict['Home'])
        self.content_panel.add_component(Home())
        self.title.content = 'Palpant Group'
        
    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(TRIAGE())
        for navg_button in self.navg_buttons:
            navg_button.role = 'default'
        self.button_1.role = 'tonal-button'
        self.title.content = 'TRIAGE'

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(EpiCops())
        for navg_button in self.navg_buttons:
            navg_button.role = 'default'
        self.button_2.role = 'tonal-button'
        self.title.content = 'EpiCops'
    

    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(CMPortal())
        for navg_button in self.navg_buttons:
            navg_button.role = 'default'
        self.button_3.role = 'tonal-button'
        self.title.content = 'CMPortal'
        
    def button_4_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(UnTANGLeD())
        for navg_button in self.navg_buttons:
            navg_button.role = 'default'
        self.button_4.role = 'tonal-button'
        self.title.content = 'UnTANGLeD'

    def button_5_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(Home())
