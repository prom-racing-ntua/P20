#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty, BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

#custom class imports
from color_block import Color_Block

Builder.load_string('''
<Brake_Bias>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.center_y, self.width, 1
    Label:
        text: "Back --- Brake Bias --- Front"
        color: 1,1,1,1
        pos_hint: {"x":0, "y":0}
        size_hint: 1, 0.4
        font_size: "16sp"
    Color_Block:
        color: 1,0,0.5,1
        pos_hint: {"center_x":root.percentage/100, "center_y":0.5}
        size_hint: 0.1, 0.3
    BoxLayout:
        orientation: "horizontal"
        pos_hint: {"x":0, "y":0.7}
        size_hint: 1, 0.1
        Label:
            text: "0"
            font_size: "8sp"
        Label:
            text: "25"
            font_size: "8sp"
        Label:
            text: "50"
            font_size: "8sp"
        Label:
            text: "75"
            font_size: "8sp"
        Label:
            text: "100"
            font_size: "8sp"
''')


class Brake_Bias(FloatLayout):
    """A widget 
    """
    percentage = BoundedNumericProperty(50, min=0, max=100, errorvalue=50)

    def __init__(self, **kwargs):
        super(Brake_Bias, self).__init__(**kwargs)
