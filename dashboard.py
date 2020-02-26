#library imports
import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock

#custom library imports

dash_labels = ["IMD","BMS","Inverter"]

Builder.load_string('''
<Dashboard>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
''')


class Dashboard(GridLayout):

    status = ListProperty(defaultvalue=[1,1,1])

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.cols = 2
        self.padding = 20
        for i in range(3):
            self.add_widget(Image(size_hint=(0.1,0.1), source="assets/green_dot.png"))
            self.add_widget(Label(text=dash_labels[i]))
        
        self.bind(status=self.update)

    def update(self):
        print(self.ids)

