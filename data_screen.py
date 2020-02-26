#library imports
from kivy.core.window import Window
import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout

#custom class imports
from pc_status import Pc_Status
from parametric_graph import Parametric_Graph 

class Data_Screen(Screen):
    
    data = ListProperty()

    def __init__(self, **kwargs):
        super(Data_Screen, self).__init__(**kwargs)
        self.pc_status = Pc_Status(pos_hint={"x": 0.4, "y": 0.85}, size_hint=(0.2, 0.15))
        self.speed_graph = Parametric_Graph(pos_hint={"x":0, "y":0.1}, size_hint=(0.5, 0.65), label= 'Voltage (V)')

        self.add_widget(self.pc_status)
        self.add_widget(self.speed_graph)