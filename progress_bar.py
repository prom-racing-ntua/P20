#library imports
import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

#custom class imports
from color_block import Color_Block


class  Progress_Bar(BoxLayout):
    max_value = NumericProperty()
    value = NumericProperty()
    def __init__(self, **kwargs):
        super(Progress_Bar, self).__init__(**kwargs)
        self.orientation = "vertical"
        for i in range(20):
            self.add_widget(Color_Block(color=[0,0,1,1]))
        

