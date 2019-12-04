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




class Segment(FloatLayout):
    seg_id = StringProperty()
    temp = NumericProperty()
    voltage = NumericProperty()

    def __init__(self, **kwargs):
        super(Segment, self).__init__(**kwargs)
        self.voltage_box = BoxLayout(orientation='vertical', pos_hint = {"x": 0, "y": 0.25}, size_hint = (1, 0.75))
        for i in range(7):
            self.voltage_box.add_widget(Label(text = str(i)))
        self.add_widget(self.voltage_box)
        self.temp_box = BoxLayout(orientation='horizontal', pos_hint = {"x": 0, "y": 0}, size_hint = (1, 0.25))


