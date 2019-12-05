import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import NumericProperty, ColorProperty

Builder.load_string('''
<Color_Block>:
    canvas:
        Color:
            rgba: self.color
        Rectangle:
            pos: self.pos
            size: self.size
''')


class Color_Block(Widget):
    color = ColorProperty()
    def __init__(self, **kwargs):
        super(Color_Block, self).__init__(**kwargs)
