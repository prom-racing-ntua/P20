#library imports
from kivy.core.window import Window
import kivy
from kivy.uix.screenmanager import Screen, ScreenManager

#custom class imports
from pc_status import Pc_Status


class Data_Screen(Screen):
    def __init__(self, **kwargs):
        super(Data_Screen, self).__init__(**kwargs)

        self.pc_status = Pc_Status(pos_hint={"x": 0.4, "y": 0.85}, size_hint=(0.2, 0.15))
        self.add_widget(self.pc_status)
