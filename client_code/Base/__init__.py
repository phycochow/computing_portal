from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home
from ..CMPortal import CMPortal
from ..EpiCops import EpiCops
from anvil.js.window import document

class Base(BaseTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.side_buttons = [self.CMPortal_button, self.epicops_button, self.home_button]
        
        self.activated_theme = 'Home'
        self.home_button_click()
        

    def home_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'Home':
            self.change_theme(theme='Home')
        self.change_content(theme="Home", content_page=Home())

    def epicops_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'EpiCops':
            self.change_theme(theme='EpiCops')
        self.change_content(theme="EpiCops", content_page=EpiCops())

    def CMPortal_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'CMPortal':
            self.change_theme(theme='CMPortal')
        self.change_content(theme="CMPortal", content_page=CMPortal())

    def change_theme(self, theme):
        themesDict = {'Home': ('#3A1D5F', '#EADDFF'),
                      'EpiCops': ('#3A1D5F', '#F3F2F1'),
                      'CMPortal': ('#492D2B', '#F3F2F1'),
                     }

        barColor, barTextColor = themesDict[theme]
        
        top_bar = document.querySelector('.app-bar')
        if top_bar:
            # self.test.content = 'My code works'
            top_bar.style.backgroundColor = barColor
            
        top_bar_links = document.querySelectorAll('.app-bar a')
        if top_bar_links:
            self.test.content = 'My code works'
            for link in top_bar_links:
                link.style.color = barTextColor
            # top_bar_text.style.backgroundColor = barTextColor

        top_bar_dropdown = document.querySelectorAll('.anvil-component select')
        for select in top_bar_dropdown:
            select.style.color = barTextColor

        self.activated_theme = theme

    def change_content(self, theme, content_page):
        themesDict = {'Home': (self.home_button, 
                               (True, False, False, False, False),
                               ('', '', '', '')
                               ),
                      'EpiCops': (self.epicops_button, 
                                (True, True, True, True, True),
                                ('Introduction', 'Visuals', 'Predictions', 'Clustering')
                                ),
                      'CMPortal': (self.CMPortal_button, 
                                  (True, True, True, True, True),
                                  ('Introduction', 'Database', 'Enrichments', 'Predictions')
                                ),
                     }
        activated_button, navg_toggle, navg_text = themesDict[theme]

        # Update content
        self.content_panel.clear()
        self.content_panel.add_component(content_page)
        
        # Update left side bar
        for side_button in self.side_buttons:
            side_button.role = 'default'
        activated_button.role = 'elevated-button'

        # Update top navigation bar, link functions are definied in the theme's code
        self.splitter_2.visible, self.link_5.visible, self.link_6.visible, self.link_7.visible, self.link_8.visible = navg_toggle
        self.link_5.text, self.link_6.text, self.link_7.text, self.link_8.text = navg_text

    def link_1_click(self, **event_args):
        self.change_content(theme="Home", content_page=Home())

    def link_2_click(self, **event_args):
        self.change_content(theme="Home", content_page=Home())

    def link_3_click(self, **event_args):
        self.change_content(theme="Home", content_page=Home())

    def link_4_click(self, **event_args):
        self.change_content(theme="Home", content_page=Home())

    # Dynamic links
    def link_5_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=EpiCops())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=CMPortal())

    def link_6_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=EpiCops())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=CMPortal())

    def link_7_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=EpiCops())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=CMPortal())

    def link_8_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=EpiCops())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=CMPortal())





        