from ._anvil_designer import EnrichmentsTemplate
from anvil import *
import anvil.server


class Enrichments(EnrichmentsTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # CMPortal TopNavgBar theme
        self.navg_toggle = (True, True, True, True, True)
        self.navg_text = ('Introduction', 'Database', 'Enrichments', 'Predictions', 'More')

        # Any code you write here will run before the form opens.
        self.column_panel_1.role = "well-style"


    def create_tabs(self):

        self.tabs_1.clear()
        
        self.tabs_lst = ['tab1', 'tab2', 'tab10']

        # Create a dictionary to store tabs and content
        self.tab_content = {}
        
        for tab_name in self.tabs_lst:
            # Create a button for the tab
            tab_button = Button(text=tab_name, role="raised-button")
            tab_button.set_event_handler('click', self.tab_button_click)
            
            # Create a Label or content for the tab
            tab_content = Label(text=f"Content for {tab_name}", visible=False)
            
            # Add button and content to the ColumnPanel
            self.tabs_1.add_component(tab_button)
            self.tabs_1.add_component(tab_content)
            
            # Store the content in the dictionary for toggling
            self.tab_content[tab_name] = tab_content
        
    def tab_button_click(self, sender, **event_args):
        # Toggle visibility of the corresponding tab content
        for tab_name, content in self.tab_content.items():
            content.visible = (sender.text == tab_name)