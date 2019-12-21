#library imports
import kivy
from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

#custom class imports
from progress_bar import Progress_Bar


class RpmBar(FloatLayout):
    value = NumericProperty()
    max_value = NumericProperty()
    color = ColorProperty()
    active_blocks = NumericProperty()
    name = StringProperty()

    def __init__(self, **kwargs):
        super(RpmBar, self).__init__(**kwargs)
        self.label = Label (text=str(self.value),color = [0,1,0,1], pos_hint={"x":0.45,"y":0.5},size_hint=(1,0.1),font_size = "35sp")
        self.active_blocks = (self.value*20)/self.max_value
        self.progress = Progress_Bar(pos_hint={"x":0, "y":0.15}, size_hint=(0.9, 0.9), orientation = "horizontal", color=self.color, active_blocks=20)


        self.add_widget(self.progress)
        self.add_widget(self.label)
