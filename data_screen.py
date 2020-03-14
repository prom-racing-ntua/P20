#library imports
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from configparser import ConfigParser

#custom class imports
from pc_status import Pc_Status
from parametric_graph import Parametric_Graph 
from histogram import Histogram

class Data_Screen(Screen):
    
    data = ListProperty()

    def __init__(self, **kwargs):
        super(Data_Screen, self).__init__(**kwargs)
        config = ConfigParser()
        config.read('config.ini')
        cfgs = config['histogram_values']

        self.pc_status = Pc_Status(pos_hint={"x": 0.4, "y": 0.85}, size_hint=(0.2, 0.15))
        self.volt_histogram = Histogram(pos_hint={"x":0, "y":0.1}, size_hint=(0.5, 0.65), label= 'Voltage (V)', 
        boundaries= [300, 600, 0, 10], histogram_points = int(cfgs['voltage_histogram_points']))

        self.add_widget(self.pc_status)
        self.add_widget(self.volt_histogram)

        self.bind(data=self.update)

    def update(self, obj, value):
        if self.data:
            self.volt_histogram.update_graph = int(self.data[7])
