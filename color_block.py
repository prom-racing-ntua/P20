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
    """A widget representing a solid colored rectangle \n
        Type:Widget
    \n
    Parameters: \n
        color: ColorProperty(list of 3 or 4 floats between (0.0-1.0) representing [red,green,blue,alpha])
        opacity: set opacity to 1 to activate or to 0 to deactivate
    """
    color = ColorProperty()
    def __init__(self, **kwargs):
        super(Color_Block, self).__init__(**kwargs)
