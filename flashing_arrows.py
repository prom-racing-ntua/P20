import kivy
kivy.require('1.10.1')
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


Builder.load_string('''
<Flashing_Arrows>:
    orientation: "vertical"
    canvas.before:
        Color:
            rgba: 0,0,1,1
        Line:
            width: 3
            rectangle: self.x, self.y, self.width, self.height
    Label:
        canvas:
            Color:
                rgba: 1,0,0,1
            Line:
                width: 2
                points: 0,0 , 1,1
''')
class Flashing_Arrows(BoxLayout):
    def __init__(self, **kwargs):
        super(Flashing_Arrows, self).__init__(**kwargs)
        

