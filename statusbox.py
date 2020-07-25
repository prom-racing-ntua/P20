#library imports
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from configparser import ConfigParser
import random
from kivy.uix.label import Label

#custom library imports
from status_block import Status_Block


Builder.load_string('''
<StatusBox>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width:1.25
''')


class StatusBox(FloatLayout):
    '''Box for status displaying'''
    labels = ListProperty()
    status = ListProperty()

    config = ConfigParser()
    config.read('config.ini')
    cfgs = config['diagnostics']

    def __init__(self, **kwargs):
        super(StatusBox, self).__init__(**kwargs)

        self.dashboard = Status_Block(size_hint=(1, 0.3), pos_hint={'x': 0, 'y': 0.7}, labels=self.cfgs['labels_dash'].split(','), colors=self.cfgs['colors_dash'].split(','))

        self.add_widget(self.dashboard)

        #self.bind()

    def update(self, obj, value):
        pass
        
