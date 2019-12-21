#library imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from datetime import datetime

#custom class imports
#from pc_battery import Pc_Battery

Builder.load_string('''
<Pc_Status>:
    Image:
        size_hint: 0.3, 1
        pos_hint: {"x":0.45, "y":0}
        source: "assets/icon.png"
        opacity: 1
''')


class Pc_Status(FloatLayout):
    def __init__(self, **kwargs):
        super(Pc_Status, self).__init__(**kwargs)
        now = datetime.now()
        self.dt = Label(text=now.strftime("%x")+", "+now.strftime("%X"), pos_hint={"x":0, "y":0.1}, size_hint=(0.5, 0.8))
        #self.battery = Pc_Battery(pos_hint={"x":0.85, "y":0.3}, size_hint=(0.2, 0.4))
        self.add_widget(self.dt)
        #self.add_widget(self.battery)
