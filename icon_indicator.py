import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


Builder.load_string('''
<Icon_Indicator>:
    Image:
        #id: img
        #size_hint: 0.6,1
        pos_hint: {"x":0,"y":0}
        source: root.source
        color: [1,0,0,1]
        #opacity: 1
    Label:
        #id: name
        size_hint: 0.4,0.5
        pos_hint: {"x":0.3,"y":0.4}
        text: root.name
        font_size: "16sp"
        color: [0,1,0,1]
    Label:
        id: value
        size_hint: 0.4,0.5
        pos_hint: {"x":0.3,"y":0.2}
        text: str(root.value)
        font_size: "24sp"
        color: [0,1,0,1]
''')


class Icon_Indicator(FloatLayout):
    value = NumericProperty()
    source = StringProperty()
    name = StringProperty()
    color = ColorProperty()

    def __init__(self, **kwargs):
        super(Icon_Indicator, self).__init__(**kwargs)
