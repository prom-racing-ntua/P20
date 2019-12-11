#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout

#custom class imports
from color_block import Color_Block
from progress_bar import Progress_Bar

class Parametric_Bar(FloatLayout):
    name = StringProperty()
    value = NumericProperty()
    max_value = NumericProperty()
    orientation = StringProperty()
    color = ColorProperty()
    active_blocks = NumericProperty()

    def __init__(self, **kwargs):
        super(Parametric_Bar, self).__init__(**kwargs)
        #calculating active sectors (x/20)
        self.active_blocks = (self.value*20)/self.max_value
        #setting up widgets
        self.label = Label(text=self.name, pos_hint={"x":0, "y":0}, size_hint=(1, 0.1))
        self.progress = Progress_Bar(pos_hint={"x":0, "y":0.15}, size_hint=(0.5, 0.9), orientation = self.orientation, color=self.color, active_blocks=self.active_blocks)
        self.val = Label(text=str(self.value), color=self.color, pos_hint={"x":0.6, "y":0.1}, size_hint=(0.4, 0.9), font_size="24sp")
        
        #adding widgets
        self.add_widget(self.label)
        self.add_widget(self.progress)
        self.add_widget(self.val)

