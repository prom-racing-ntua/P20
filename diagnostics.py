#library imports
from kivy.core.window import Window
import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty

#custom class imports
from pc_status import Pc_Status


class Diagnostics(Screen):
    data = ListProperty()
