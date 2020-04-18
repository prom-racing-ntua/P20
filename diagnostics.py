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

    test1 = StringProperty()

    def __init__(self, **kwargs):
        super(Diagnostics, self).__init__(**kwargs)

        self.test1 = "same"

        self.rv = RV(pos_hint={"x": 0.05, "y": 0.02}, size_hint=(0.9, 0.2))
        self.add_widget(self.rv)

        self.tabs = Datatabs(pos_hint={"x": 0.05, "y": 0.25}, size_hint=(0.9, 0.65))
        self.add_widget(self.tabs)

        self.bind(data=self.errorgen)
        self.bind(test1=self.errorgen)
        Clock.schedule_interval(self.test, 0.5)

    def errorgen(self, obj, value):
        #print(value)
        #apps validation
        if not (0 <= self.data[0] <= int(self.cfgs['apps_max'])):
            self.rv.new_error = 'apps value: {val} out of bounds (0-{mx})'.format(val=self.data[0], mx=self.cfgs['apps_max'])
            #self.rv.data.append({'apps value: {val} out of bounds (0-{mx})'.format(val=self.data[0], mx=self.cfgs['apps_max'])})
        #brake validation
        if not (0 <= self.data[1] <= int(self.cfgs['brake_max'])):
            self.rv.new_error = 'brake value: {val} out of bounds (0-{mx})'.format(val=self.data[1], mx=self.cfgs['brake_max'])
            #self.rv.data.append({'brake value: {val} out of bounds (0-{mx})'.format(val=self.data[1], mx=self.cfgs['brake_max'])})

    def test(self, dt):
        self.test1 = "same1"
        #print(self.parent)
        #self.data[0] = 30
        #self.data[1] = 30
        #self.data[0] = random.randint(-10,130)
        #self.data[1] = random.randint(-10,130)


