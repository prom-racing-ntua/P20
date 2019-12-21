import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty



Builder.load_string("""
<Time_Label>:
    text: self.colortime
    color:self.colortext
    canvas:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle:self.x,self.y,self.width,self.height
            width:1.25
""")


class Time_Label(Label):
    colortime = StringProperty()
    colortext = ColorProperty()
    def __init__(self,**kwargs):
        super(Time_Label,self).__init__(**kwargs)
