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
from tabs import Tabs


Builder.load_string('''
<Middle>:
    canvas.before:
        Color:
            rgba: 1,0,0,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
    Label:
        pos_hint: {"top":1, "x":0.3}
        size_hint: 0.2, 0.1
        text: "middle"
    Tabs:
        pos_hint: {"top": .9, "x": 0}
        size_hint: 1, 0.7
''')



class Middle(FloatLayout):
    def __init__(self, **kwargs):
        super(Middle, self).__init__(**kwargs)
