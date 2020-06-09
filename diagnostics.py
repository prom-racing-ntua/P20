#library imports
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from configparser import ConfigParser
import random


#custom class imports
from pc_status import Pc_Status
from errorbar import RV
from datatabs import Datatabs

Builder.load_string('''
<Diagnostics>:
''')

class Diagnostics(Screen):
    data = ListProperty([0,0])
    errors = ListProperty([''])
    config = ConfigParser()
    config.read('config.ini')
    cfgs = config['sensor_values']


    def __init__(self, **kwargs):
        super(Diagnostics, self).__init__(**kwargs)

        self.rv = RV(pos_hint={"x": 0.05, "y": 0.02}, size_hint=(0.9, 0.2))
        self.add_widget(self.rv)

        self.tabs = Datatabs(pos_hint={"x": 0.05, "y": 0.25}, size_hint=(0.9, 0.65))
        self.add_widget(self.tabs)

        #self.bind(errors=self.streamline_errors)
        self.bind(data=self.update_data)
        self.bind(errors=self.update_errors)


    def streamline_errors(self, obj, value):
        for i in self.errors:
            self.rv.new_error = "timestamp: " + i['timestamp'] + " error at pos: " + str(i['datapos']) + " value: " + str(i['value'])
        self.errors = []

    def update_data(self, obj, value):
        for i in range(len(self.data)):
            self.tabs.items[i].data = self.data[i]
    
    def update_errors(self, obj, value):
        for i in range(len(self.errors)):
            self.tabs.items[i].status = self.errors[i]





