from ._anvil_designer import CMPortalTemplate
from anvil import *

from .Database import Database
from .Enrichments import Enrichments
from .More import More
from .Predictions import Predictions

class CMPortal(CMPortalTemplate):
    def __init__(self, base, **properties):
        self.base = base
        self.init_components(**properties)
        
        # CMPortal TopNavgBar theme
        self.navg_toggle = (True, True, True, True, True)
        self.navg_text = ('Introduction', 'Database', 'Enrichments', 'Predictions', 'More')
        
        self.column_panel_1.role = "well-style"
        self.column_panel_2.role = "well-style"
        self.column_panel_3.role = "well-style"

        self.link_1.role = "CMPortalButton"
        self.link_2.role = "CMPortalButton"
        self.link_3.role = "CMPortalButton"


    def browseProtocol_click(self, **event_args):
        self.base.change_content(Database(self.base))  # top navigation bar is not updated as default
        self.base.refresh_navgBar(self.base.link_6)

    def exploreFindings_click(self, **event_args):
        self.base.change_content(Enrichments(self.base))
        self.base.refresh_navgBar(self.base.link_7)

    def downloadData_click(self, **event_args):
        self.base.change_content(More(self.base))
        self.base.refresh_navgBar(self.base.link_9)


    