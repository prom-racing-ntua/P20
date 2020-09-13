#library imports
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from configparser import ConfigParser


#custom library imports


led_colors = ["assets/green_dot.png",
              "assets/red_dot.png", "assets/pink_dot.png"]

Builder.load_string('''
<Status_Block>:
    cols: 6
        
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: root.x, root.y, root.width , root.height
    
''')


class Status_Block(GridLayout):
    """
    colors: 0=green, 1=red, 2=pink
    """

    labels = ListProperty()
    status = ListProperty([])
    leds = ListProperty()
    colors = ListProperty()

    def __init__(self, **kwargs):
        super(Status_Block, self).__init__(**kwargs)
        self.padding = 10

        for i in range(len(self.labels)):
            self.add_widget(Label(text=self.labels[i]))
            self.leds.append(Image(source=led_colors[int(self.colors[i])], size_hint=(0.25, 0.25)))
            self.add_widget(self.leds[-1])

        self.bind(status=self.update)

    def update(self, obj, value):
        i = 0
        for led in self.leds:
            led.opacity = self.status[i]+0.2
            i += 1
