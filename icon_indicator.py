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
        pos_hint: {"x":0,"y":0}
        source: root.source
        opacity: root.opacity
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: root.center
        canvas.after:
            PopMatrix
        
    Label:
        size_hint: 0.4,0.2
        pos_hint: {"x":0.3,"y":0}
        text: root.name
        font_size: "16sp"
        color: [1,1,1,1]
    Label:
        size_hint: 0.4,0.5
        pos_hint: {"x":0.3,"y":0.25}
        text: str(root.value)+root.unit
        font_size: "24sp"
        color: root.color
''')


class Icon_Indicator(FloatLayout):
    angle = NumericProperty()
    value = NumericProperty()
    unit = StringProperty()
    opacity = NumericProperty()
    source = StringProperty()
    name = StringProperty()
    color = ColorProperty()
    boundaries = ListProperty()
    icon_update = NumericProperty()

    def __init__(self, **kwargs):
        super(Icon_Indicator, self).__init__(**kwargs)
        self.bind(icon_update=self.update)
        self.bind(value=self.update)

    def update(self, obj, val):
        if (self.unit == '°'):
            self.angle = val
        else:
            if (self.value>=self.boundaries[1]):
                self.color = [1,0,0,1]
            elif (self.value>=self.boundaries[0]):
                self.color = [1,0.5,0,1]
            else:
                self.color = [1,1,1,1]
        self.value = val
    
