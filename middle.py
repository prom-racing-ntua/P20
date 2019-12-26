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
from kivy.clock import Clock

#custom class imports
from parametric_bar import Parametric_Bar
from pc_status import  Pc_Status
from rpmbar import RpmBar
from icon_indicator import Icon_Indicator

class Middle(FloatLayout):
    def __init__(self, **kwargs):
        super(Middle, self).__init__(**kwargs)

        #setting up widgets
        self.pc_status = Pc_Status(pos_hint={"x":0.05, "y":0.85}, size_hint=(1, 0.15))
        self.tps = Parametric_Bar(pos_hint={"x":0.05, "y":0.35}, size_hint=(0.2, 0.13), name="TPS(%)", value=30, max_value=100, color=[0,1,0,1], orientation="vertical")
        self.brake = Parametric_Bar(pos_hint={"x":0.3, "y":0.35}, size_hint=(0.2, 0.13), name="Brake(%)", value=5, max_value=100, color=[1,0,0,1], orientation="vertical")
        self.bias = Parametric_Bar(pos_hint={"x":0.05, "y":0.15}, size_hint=(0.4, 0.05), name="Brake Bias(%)", value=10, max_value=100, color=[1,0,1,1], orientation="horizontal")
        self.rpmbar = RpmBar(pos_hint ={"x":0.05, "y":0.5},size_hint= (0.8, 0.13), name = "Rpm(%)", value=8500, max_value=10000, color=[1,0,0,1])
        self.motor_temp = Icon_Indicator(pos_hint ={"x":0.5, "y":0}, size_hint= (0.5, 0.4), name = "Motor Temp", value = 50, source = "assets/motor.png")
        
        #adding widgets
        self.add_widget(self.pc_status)
        self.add_widget(self.tps)
        self.add_widget(self.brake)
        self.add_widget(self.bias)
        self.add_widget(self.rpmbar)
        self.add_widget(self.motor_temp)

