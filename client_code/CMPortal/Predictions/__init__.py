from ._anvil_designer import PredictionsTemplate
from anvil import *
import anvil.server


class Predictions(PredictionsTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # CMPortal TopNavgBar theme
        self.navg_toggle = (True, True, True, True, True)
        self.navg_text = ('Introduction', 'Database', 'Enrichments', 'Predictions', 'More')

        # Any code you write here will run before the form opens.
