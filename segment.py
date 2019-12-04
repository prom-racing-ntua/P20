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

Builder.load_string('''
<Segment>:
    Label:
        text: "smt"
''')


class Segment(FloatLayout):
    seg_id = StringProperty()
    temp = NumericProperty()
    voltage = NumericProperty()

    def __init__(self, **kwargs):
        super(Segment, self).__init__(**kwargs)
