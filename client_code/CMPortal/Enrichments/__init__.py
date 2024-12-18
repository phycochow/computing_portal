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
        
