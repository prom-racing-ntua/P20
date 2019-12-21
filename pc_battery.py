#library imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
#import psutil
#custom class imports
from color_block import Color_Block

Builder.load_string('''
<Pc_Battery>:
    canvas:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
''')

class Pc_Battery(BoxLayout):
    battery = ObjectProperty()
    def __init__(self, **kwargs):
        super(Pc_Battery, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.spacing = 5
        self.battery = psutil.sensors_battery()
        print(self.battery.percent)
        for i in range(4, -1, -1):
            a = 0 if (4-i)*20 >= self.battery.percent else 1
            self.add_widget(Color_Block(color=[1,1,1,a]))
