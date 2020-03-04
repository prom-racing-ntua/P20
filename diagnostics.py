#library imports
from kivy.core.window import Window
import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty

#custom class imports
from pc_status import Pc_Status
from errormessages import ErrorMessages


class Diagnostics(Screen):
    data = ListProperty()

    def __init__(self, **kwargs):
        super(Diagnostics, self).__init__(**kwargs)
    
        errors = ErrorMessages(size_hint=[1,0.5])
        self.add_widget(errors)
        print(self.children)
