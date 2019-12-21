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
from parametric_bar import Parametric_Bar
from pc_status import  Pc_Status


class Middle(FloatLayout):
    def __init__(self, **kwargs):
        super(Middle, self).__init__(**kwargs)

        #setting up widgets
        self.pc_status = Pc_Status(pos_hint={"x":0.05, "y":0.85}, size_hint=(1, 0.15))
        self.tps = Parametric_Bar(pos_hint={"x":0.05, "y":0.35}, size_hint=(0.2, 0.13), name="TPS(%)", value=30, max_value=100, color=[0,1,0,1], orientation="vertical")
        self.brake = Parametric_Bar(pos_hint={"x":0.3, "y":0.35}, size_hint=(0.2, 0.13), name="Brake(%)", value=5, max_value=100, color=[1,0,0,1], orientation="vertical")
        self.bias = Parametric_Bar(pos_hint={"x":0.05, "y":0.15}, size_hint=(0.4, 0.05), name="Brake Bias(%)", value=10, max_value=100, color=[1,0,1,1], orientation="horizontal")

        #adding widgets
        self.add_widget(self.pc_status)
        self.add_widget(self.tps)
        self.add_widget(self.brake)
        self.add_widget(self.bias)
