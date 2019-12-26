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
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock


#custom class imports
from tire_temps import Tire_Temps
from battery import Battery
from battery_graph import Battery_Graph
from parametric_bar import Parametric_Bar

class Left(FloatLayout):
    data = ListProperty()
    def __init__(self, **kwargs):
        super(Left, self).__init__(**kwargs)

        self.data = [600,0]

        #setting up widgets
        self.tire_temps = Tire_Temps(pos_hint={"bottom": 1, "left": 0.95}, size_hint=(1, 0.3))
        self.battery = Battery_Graph(pos_hint={"x":0, "y":0.32}, size_hint=(1, 0.5), points=[(600,0)])
        self.kw = Parametric_Bar(pos_hint={"x":0.05, "y":0.85}, size_hint=(0.2, 0.13), name="Power(kW)", value=50, max_value=100, color=[0,0,1,1], orientation="vertical")
        self.cur = Parametric_Bar(pos_hint={"x":0.3, "y":0.85}, size_hint=(0.2, 0.13), name="Current(A)", value=0, max_value=100, color=[0,0,1,1], orientation="vertical")
        self.vol = Parametric_Bar(pos_hint={"x":0.55, "y":0.85}, size_hint=(0.2, 0.13), name="Voltage(V)", value=100, max_value=100, color=[0,0,1,1], orientation="vertical")
        
        #adding widgets
        self.add_widget(self.battery)
        self.add_widget(self.tire_temps)
        self.add_widget(self.kw)
        self.add_widget(self.cur)
        self.add_widget(self.vol)

        #self.bind(data=self.update_data)

    def update_data(self):
        print("left")
        self.battery.points = (self.data[0],self.data[1])
