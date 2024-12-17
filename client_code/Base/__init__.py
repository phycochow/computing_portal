from anvil import *
from ._anvil_designer import BaseTemplate
from anvil.js.window import document

from ..Home import Home
from ..Home.People import People
from ..Home.News import News

from ..EpiCops import EpiCops
from ..EpiCops.FunVisuals import FunVisuals
from ..EpiCops.Clustering import Clustering
from ..EpiCops.ModelTraining import ModelTraining
from ..EpiCops.Store import Store

from ..CMPortal import CMPortal
from ..CMPortal.Database import Database
from ..CMPortal.Enrichments import Enrichments
from ..CMPortal.Predictions import Predictions
from ..CMPortal.More import More
from ..Home.Contacts import Contacts

class Base(BaseTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.side_buttons = [self.CMPortal_button, self.epicops_button, self.home_button]
        self.navgLinks = [self.link_1, self.link_2, self.link_3, self.link_4, self.link_5, self.link_6, self.link_7, self.link_8, self.link_9]
        self.themesDict = {'Home': ('#3A1D5F', '#6750A4', '#EADDFF'),
                      'EpiCops': ('#3A1D5F', '#6750A4', '#EADDFF'),
                      'CMPortal': ('#492D2B', '#C2AF77', '#F3F2F1'),
                     }
        self.activated_theme = 'Home'
        self.home_button_click()

    def home_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'Home':
            self.change_theme(theme='Home')
        self.change_content(theme="Home", content_page=Home())
        self.refresh_navgBar(self.link_2)

    def epicops_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'EpiCops':
            self.change_theme(theme='EpiCops')
        self.change_content(theme="EpiCops", content_page=EpiCops())
        self.refresh_navgBar(self.link_5)

    def CMPortal_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'CMPortal':
            self.change_theme(theme='CMPortal')
        self.change_content(theme="CMPortal", content_page=CMPortal())
        self.refresh_navgBar(self.link_5)

    def change_theme(self, theme):
        barColor, barActiveColor, barTextColor = self.themesDict[theme]
        top_bar = document.querySelector('.app-bar')
        if top_bar:
            top_bar.style.backgroundColor = barColor
            top_bar.style.setProperty('--appbar-hover-bg', barActiveColor)
            
        top_bar_links = document.querySelectorAll('.app-bar a')
        if top_bar_links:
            self.test.content = 'My code works'
            for link in top_bar_links:
                link.style.color = barTextColor

        self.activated_theme = theme
        self.refresh_navgBar(None)

    def change_content(self, theme, content_page):
        themesDict = {'Home': (self.home_button, 
                               (True, False, False, False, False, False),
                               ('', '', '', '', '')
                               ),
                      'EpiCops': (self.epicops_button, 
                                (True, True, True, True, True, True),
                                ('About', 'Visuals', 'Predictions', 'Clustering', 'Store')
                                ),
                      'CMPortal': (self.CMPortal_button, 
                                  (True, True, True, True, True, True),
                                  ('Introduction', 'Database', 'Enrichments', 'Predictions', 'More')
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
        self.splitter_2.visible, self.link_5.visible, self.link_6.visible, self.link_7.visible, self.link_8.visible, self.link_9.visible = navg_toggle
        self.link_5.text, self.link_6.text, self.link_7.text, self.link_8.text, self.link_9.text = navg_text

    def refresh_navgBar(self, target_link=None):
        barColor, barActiveColor, _ = self.themesDict[self.activated_theme]
        for link in self.navgLinks:
            link.background = barColor
        if target_link:
            target_link.background = barActiveColor 
    
    def link_1_click(self, **event_args):
        self.change_content(theme=self.activated_theme, content_page=Home())
        self.refresh_navgBar(self.link_2)

    def link_2_click(self, **event_args):
        self.change_content(theme=self.activated_theme, content_page=Home())
        self.refresh_navgBar(self.link_2)

    def link_3_click(self, **event_args):
        self.change_content(theme=self.activated_theme, content_page=News())
        self.refresh_navgBar(self.link_3)

    def link_4_click(self, **event_args):
        self.change_content(theme=self.activated_theme, content_page=People())
        self.refresh_navgBar(self.link_4)

    # Dynamic links
    def link_5_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=EpiCops())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=CMPortal())
        self.refresh_navgBar(self.link_5)
        
    def link_6_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=FunVisuals())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=Database())
        self.refresh_navgBar(self.link_6)

    def link_7_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=ModelTraining())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=Enrichments())
        self.refresh_navgBar(self.link_7)
        
    def link_8_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=Clustering())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=Predictions())
        self.refresh_navgBar(self.link_8)

    def link_9_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(theme="EpiCops", content_page=Store())
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=More())
        self.refresh_navgBar(self.link_9)

    def link_10_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.change_content(theme="Home", content_page=Contacts())
        self.refresh_navgBar(self.link_10)





        