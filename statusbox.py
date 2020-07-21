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


Builder.load_string('''
<StatusBox>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width:1.25
''')


class StatusBox(GridLayout):
    '''Box for status displaying'''
    labels = ListProperty()
    status = ListProperty()

    def __init__(self, **kwargs):
        super(StatusBox, self).__init__(**kwargs)

        #self.bind()

    def update(self, obj, value):
        pass
        
