import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty

from color_block import Color_Block


class Segment(FloatLayout):
    seg_id = StringProperty()
    temp = NumericProperty()
    voltage = NumericProperty()

    def __init__(self, **kwargs):
        super(Segment, self).__init__(**kwargs)
        self.voltage_box = BoxLayout(orientation='vertical', pos_hint = {"x": 0, "y": 0.35}, size_hint = (1, 0.65), spacing = 5)
        #self.voltage_labels = BoxLayout()
        #self.voltage_box.canvas.before.add(Color(1,1,1,1))
        #self.voltage_box.canvas.before.add(Line(rectangle=(self.voltage_box.x, self.voltage_box.y, self.voltage_box.width, self.voltage_box.height)))
            #Color(1,1,1,1)
            #self.voltage_box.line = Line(rectangle=(self.voltage_box.x, self.voltage_box.y, self.voltage_box.width, self.voltage_box.height))
        self.voltage_label = Label(text=str(self.voltage)+"V")
        self.voltage_box.add_widget(self.voltage_label)
        for i in range(10):
            self.voltage_box.add_widget(Color_Block(color=(0,1,0,1)))
        
        self.add_widget(self.voltage_box)
        self.temp_box = BoxLayout(orientation='vertical', pos_hint = {"x": 0, "y": 0}, size_hint = (1, 0.35), spacing = 0)
        for i in range(10):
            self.temp_box.add_widget(Color_Block(color=(1,0,0,1)))
        self.temp_label = Label(text=str(self.temp)+"°C")
        self.temp_box.add_widget(self.temp_label)
        self.add_widget(self.temp_box)
