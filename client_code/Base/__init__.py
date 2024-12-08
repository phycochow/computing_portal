from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home
from ..CMPortal import CMPortal
from ..EpiCops import EpiCops

class Base(BaseTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        # self.pages_dict = {'Home' : Home(), 'Epi'}

        self.navg_links = [self.link_1, self.link_2]
        self.side_buttons = [self.CMPortal_button, self.epicops_button, self.home_button]

        # self.content_panel.add_component(self.pages_dict['Home'])
        self.home_button_click()

    def home_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(Home())

        # Update left side bar
        for side_button in self.side_buttons:
            side_button.role = 'default'
        self.home_button.role = 'tonal-button'

        # Update top navigation bar
        self.link_4.visible = False
        self.link_5.visible = False
        self.link_6.visible = False
        self.link_7.visible = False

    def epicops_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Update content
        self.content_panel.clear()
        self.content_panel.add_component(EpiCops())

        # Update left side bar
        for side_button in self.side_buttons:
            side_button.role = 'default'
        self.epicops_button.role = 'tonal-button'

        # Update top navigation bar
        self.link_4.visible = True
        self.link_5.visible = True
        self.link_6.visible = True
        self.link_7.visible = True
        
        self.link_4.text = "Introduction"
        self.link_5.text = "Visuals"
        self.link_6.text = "Predictions"
        self.link_7.text = "Clustering"
    
    def CMPortal_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.content_panel.clear()
        self.content_panel.add_component(CMPortal())
        for side_button in self.side_buttons:
            side_button.role = 'default'
        self.CMPortal_button.role = 'tonal-button'

        # Update top navigation bar
        self.link_4.visible = True
        self.link_5.visible = True
        self.link_6.visible = True
        self.link_7.visible = True
        
        self.link_4.text = "Introduction"
        self.link_5.text = "Database"
        self.link_6.text = "Enrichments"
        self.link_7.text = "Predictions"

    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        pass
