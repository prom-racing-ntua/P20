#library imports
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from configparser import ConfigParser
import random


#custom class imports
from pc_status import Pc_Status
from errorbar import RV

Builder.load_string('''
<Diagnostics>:
    Label:
        text: "".join(root.errors)
#ScrollView:
    #do_scroll_x: False
    #do_scroll_y: True
    
    #Label:
        #size_hint: (1, None)
        #size: Window.size
        #text: "i don't know what the fuck i'm doing rn/n" * 100
''')

class Diagnostics(Screen):
    data = ListProperty([0,0])
    errors = ListProperty([''])
    #layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    config = ConfigParser()
    config.read('config.ini')
    cfgs = config['sensor_values']

    def __init__(self, **kwargs):
        super(Diagnostics, self).__init__(**kwargs)
        config = ConfigParser()
        config.read('config.ini')
        cfgs = config['sensor_values']
        #root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        
        #root.add_widget(self.layout)        
        #self.add_widget(root)
        self.rv = RV(pos_hint={"x": 0.1, "y": 0.1}, size_hint=(0.8, 0.5))
        self.add_widget(self.rv)
        self.bind(data=self.errorgen)
        Clock.schedule_interval(self.test, 0.5)

    def errorgen(self, obj, value):
        #apps validation
        if not (0 <= self.data[0] <= int(self.cfgs['apps_max'])):
            self.rv.new_error = 'apps value: {val} out of bounds (0-{mx})'.format(val=self.data[0], mx=self.cfgs['apps_max'])
            #self.rv.data.append({'apps value: {val} out of bounds (0-{mx})'.format(val=self.data[0], mx=self.cfgs['apps_max'])})
        #brake validation
        if not (0 <= self.data[1] <= int(self.cfgs['brake_max'])):
            self.rv.new_error = 'brake value: {val} out of bounds (0-{mx})'.format(val=self.data[1], mx=self.cfgs['brake_max'])
            #self.rv.data.append({'brake value: {val} out of bounds (0-{mx})'.format(val=self.data[1], mx=self.cfgs['brake_max'])})

    def test(self, dt):
        #for i in range():
        self.data[0] = random.randint(-10,130)
        self.data[1] = random.randint(-10,130)


