# importing libraries
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color, Canvas, Line
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty

Builder.load_string("""
<Track_map>:
    canvas:
        Color:
            rgb: .5,.5,.5
        Rectangle:
            pos: self.pos
            size: self.size
            source: "./assets/Tracklayout.png"
""")

class Track_map(FloatLayout):
    def __init__(self, **kwargs):
        super(Track_map, self).__init__(**kwargs)