#library imports
import kivy
from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


#custom class imports
from progress_bar import Progress_Bar
from color_block import Color_Block

Builder.load_string('''
<RpmBar>:
    canvas.before:
        Color:
            rgba: 1,1,1,0.5
        Line:
            rectangle: self.x, self.y, self.width, self.height
        Line:
            rectangle: self.x, self.y, self.width, self.height/2
    Label:
        text: str(root.value)
        color: root.color
        pos_hint: {"x":0.4, "y":0.5}
        size_hint: 0.2, 0.5
        font_size: "24sp"
''')


class RpmBar(FloatLayout):
    value = NumericProperty()
    max_value = NumericProperty()
    color = ColorProperty()
    active_dots = NumericProperty()
    #name = StringProperty()

    def __init__(self, **kwargs):
        super(RpmBar, self).__init__(**kwargs)
        #self.label = Label (text=str(self.value),color = [0,1,0,1], pos_hint={"x":0.45,"y":0.5},size_hint=(1,0.1),font_size = "35sp")
        self.active_dots = (self.value*10)/self.max_value
        #self.progress = Progress_Bar(pos_hint={"x":0, "y":0.15}, size_hint=(0.9, 0.9), orientation = "horizontal", color=self.color, active_blocks=20)
        self.box = BoxLayout(pos_hint={"x": 0, "y": 0}, size_hint=(1, 0.5), orientation="horizontal", spacing=1.5)
        self.dots = []
        for i in range(5):
            self.dots.append(Image(source="assets/green_dot.png"))
            self.box.add_widget(self.dots[i])
        for i in range(3):
            self.dots.append(Image(source="assets/yellow_dot.png"))
            self.box.add_widget(self.dots[i+5])
        for i in range(2):
            self.dots.append(Image(source="assets/red_dot.png"))
            self.box.add_widget(self.dots[i+8])
        for i in range(2):
            self.dots.append(Image(source="assets/red_dot.png"))
            self.box.add_widget(self.dots[i+10])
        for i in range(3):
            self.dots.append(Image(source="assets/yellow_dot.png"))
            self.box.add_widget(self.dots[i+12])
        for i in range(5):
            self.dots.append(Image(source="assets/green_dot.png"))
            self.box.add_widget(self.dots[i+15])

        self.add_widget(self.box)

        self.bind(value=self.update_dots)

    def update_dots(self, obj, value):
        self.active_dots = (self.value*10)/self.max_value
        for i in range(10):
            if i < self.active_dots:
                self.dots[i].opacity = 1
                self.dots[19-i].opacity = 1
            else:
                self.dots[i].opacity = 0.2
                self.dots[19-i].opacity = 0.2
