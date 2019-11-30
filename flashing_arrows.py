import kivy
kivy.require('1.10.1')
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty

Builder.load_string('''
<Flashing_Arrows>:
    orientation: "vertical"
    Image:
        id: 0
        size_hint: 1,0.2
        source: "assets/3.jpg"
        opacity: 0.1 
    Image:
        id: 1
        size_hint: 1,0.2
        source: "assets/3.jpg"
        opacity: 0.1 
    Image:
        id: 2
        size_hint: 1,0.2
        source: "assets/3.jpg"
        opacity: 0.1
    Image:
        id: 3
        size_hint: 1,0.2
        source: "assets/3.jpg"
        opacity: 0.1
    Image:
        id: 4
        size_hint: 1,0.2
        source: "assets/3.jpg"
        opacity: 0.1         
''')



class Flashing_Arrows(BoxLayout):
    active = NumericProperty()
    def __init__(self, **kwargs):
        super(Flashing_Arrows, self).__init__(**kwargs)
        self.active = 4
        Clock.schedule_interval(self.next_arrow, 0.3)

    def next_arrow(self, dt):
        self.ids[str(self.active)].opacity = 0.15
        self.active -= 1
        if self.active < 0:
            self.active = 4
        self.ids[str(self.active)].opacity = 0.8

