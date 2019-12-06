#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

#custom class imports
from tire_temps import Tire_Temps
from battery import Battery
from battery_graph import Battery_Graph

Builder.load_string('''
<Left>:
    Label:
        pos_hint: {"top":1, "x":0.3}
        size_hint: 0.2, 0.2
        text: "left"
    Tire_Temps:
        pos_hint: {"bottom":1, "left":0.95}
        size_hint: 1, 0.3
    #Battery_Graph:
        #pos_hint: {"x":0, "y":0.32}
        #size_hint: 1, 0.5
        #points: [(0,588),(5,548),(10,500),(15,452)]
''')

class Left(FloatLayout):
    def __init__(self, **kwargs):
        super(Left, self).__init__(**kwargs)
        self.battery = Battery_Graph(pos_hint={"x":0, "y":0.32}, size_hint=(1, 0.5), points=[(0,588),(5,548),(10,500),(15,452)])
        self.add_widget(self.battery)

