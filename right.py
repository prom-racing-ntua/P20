import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Mesh


class Right(FloatLayout):
    def __init__(self, **kwargs):
        super(Right, self).__init__(**kwargs)
        with self.canvas:
            Color(1,0,0,1)
            Mesh(mode='triangle_fan', indices=[0,1,2])
            #self.line = Line(width= 3, rectangle =( self.x, self.y, self.width, self.height))

