import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty, NumericProperty

Builder.load_string("""
<Status_Label>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle:self.x,self.y,self.width,self.height
            width:1.25
        Color:
            rgba: root.color
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: root.label
        pos_hint: {"x":0, "y":0.7}
        size_hint: 1, 0.3
        #font_size: "24sp"
    Label:
        text: root.data
        pos_hint: {"x":0, "y":0}
        size_hint: 1, 0.7
        #font_size: "24sp"
""")


class Status_Label(FloatLayout):
    label = StringProperty()
    data = StringProperty()
    status = NumericProperty()
    color = ColorProperty([0,1,0,0.5])

    def __init__(self, **kwargs):
        super(Status_Label, self).__init__(**kwargs)
        self.bind(status = self.update_status)

    def update_status(self, obj, value):
        if self.status == 0:
            self.color = [0,1,0,0.5]
        elif self.status == 1:
            self.color = [1,0.647,0,0.5]
        else:
            self.color = [1,0,0,0.5]
