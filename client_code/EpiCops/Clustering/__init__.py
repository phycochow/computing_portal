from ._anvil_designer import ClusteringTemplate
from anvil import *
import anvil.server


class Clustering(ClusteringTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # CMPortal TopNavgBar theme
        self.navg_toggle = (True, True, True, True, True)
        self.navg_text = ('About', 'Visuals', 'Predictions', 'Clustering', 'Store')

        # Any code you write here will run before the form opens.
