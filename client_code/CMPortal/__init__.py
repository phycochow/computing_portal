from ._anvil_designer import CMPortalTemplate
from anvil import *


class CMPortal(CMPortalTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.column_panel_1.role = "well-style"
        self.column_panel_2.role = "well-style"
        self.column_panel_3.role = "well-style"

        self.link_1.role = "CMPortalButton"
        self.link_2.role = "CMPortalButton"
        self.link_3.role = "CMPortalButton"
        # Any code you write here will run before the form opens.
