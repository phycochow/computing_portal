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
        self.themeColours = {'Home': ('#3A1D5F', '#6750A4', '#EADDFF'),
                      'EpiCops': ('#3A1D5F', '#6750A4', '#EADDFF'),
                      'CMPortal': ('#492D2B', '#C2AF77', '#F3F2F1'),
                     }
        self.activated_theme = 'Home'
        self.content = None  # sets to Home(self) due to next line
        self.home_button_click()

    def home_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'Home':
            self.change_theme('Home')
        self.change_content(Home(self), TopNavgUpdate=True)
        self.refresh_navgBar(self.link_2)

    def epicops_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'EpiCops':
            self.change_theme('EpiCops')
        self.change_content(EpiCops(self), TopNavgUpdate=True)
        self.refresh_navgBar(self.link_5)

    def CMPortal_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.activated_theme != 'CMPortal':
            self.change_theme('CMPortal')
        self.change_content(CMPortal(self), TopNavgUpdate=True)
        self.refresh_navgBar(self.link_5)

    def change_theme(self, theme):
        self.activated_theme = theme
        barColor, barActiveColor, barTextColor = self.themeColours[self.activated_theme]
        top_bar = document.querySelector('.app-bar')
        if top_bar:
            top_bar.style.backgroundColor = barColor
            top_bar.style.setProperty('--appbar-hover-bg', barActiveColor)
            
        top_bar_links = document.querySelectorAll('.app-bar a')
        if top_bar_links:
            self.test.content = 'My code works'
            for link in top_bar_links:
                link.style.color = barTextColor

        self.refresh_navgBar(None)

    def change_content(self, content_page, TopNavgUpdate=False):
        self.content = content_page
        
        if self.activated_theme == 'Home':
            activated_button = self.home_button
        elif self.activated_theme == 'EpiCops':
            activated_button = self.epicops_button
        elif self.activated_theme == 'CMPortal':
            activated_button = self.CMPortal_button
        
        # Update content
        self.content_panel.clear()
        self.content_panel.add_component(self.content)
            
        # Update left side bar
        for side_button in self.side_buttons:
            side_button.role = 'default'
        activated_button.role = 'elevated-button'
        
        if TopNavgUpdate:
            # Update top navigation bar, link functions are definied in the theme's code
            self.link_5.visible, self.link_6.visible, self.link_7.visible, self.link_8.visible, self.link_9.visible = self.content.navg_toggle
            self.link_5.text, self.link_6.text, self.link_7.text, self.link_8.text, self.link_9.text = self.content.navg_text

    def refresh_navgBar(self, target_link=None):
        barColor, barActiveColor, _ = self.themeColours[self.activated_theme]
        for link in self.navgLinks:
            link.background = barColor
        if target_link:
            target_link.background = barActiveColor 
    
    def link_1_click(self, **event_args):
        RefreshTabs = self.activated_theme == 'Home'  # this usually hides tabs
        self.change_content(Home(self),  TopNavgUpdate=RefreshTabs)
        self.refresh_navgBar(self.link_2)

    def link_2_click(self, **event_args):
        RefreshTabs = self.activated_theme == 'Home'  # this usually hides tabs
        self.change_content(Home(self),  TopNavgUpdate=RefreshTabs)
        self.refresh_navgBar(self.link_2)

    def link_3_click(self, **event_args):
        RefreshTabs = self.activated_theme == 'Home'  # this usually hides tabs
        self.change_content(News(self),  TopNavgUpdate=RefreshTabs)
        self.refresh_navgBar(self.link_3)

    def link_4_click(self, **event_args):
        RefreshTabs = self.activated_theme == 'Home'  # this usually hides tabs
        self.change_content(People(self),  TopNavgUpdate=RefreshTabs)
        self.refresh_navgBar(self.link_4)

    # Dynamic links
    def link_5_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(EpiCops(self))
        if self.activated_theme == 'CMPortal':
            self.change_content(CMPortal(self))
        self.refresh_navgBar(self.link_5)
        
    def link_6_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(FunVisuals(self))
        if self.activated_theme == 'CMPortal':
            self.change_content(Database(self))
        self.refresh_navgBar(self.link_6)

    def link_7_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(ModelTraining(self))
        if self.activated_theme == 'CMPortal':
            self.change_content(Enrichments(self))
        self.refresh_navgBar(self.link_7)
        
    def link_8_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(Clustering(self))
        if self.activated_theme == 'CMPortal':
            self.change_content(theme="CMPortal", content_page=Predictions(self))
        self.refresh_navgBar(self.link_8)

    def link_9_click(self, **event_args):
        """This method is called when the link is clicked"""
        if self.activated_theme == 'EpiCops':
            self.change_content(Store(self))
        if self.activated_theme == 'CMPortal':
            self.change_content(More(self))
        self.refresh_navgBar(self.link_9)

    def link_10_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.change_content(Contacts(self))
        self.refresh_navgBar(self.link_10)





        