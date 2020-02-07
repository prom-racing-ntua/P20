
#library imports
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Canvas, Rectangle, RoundedRectangle, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, ColorProperty, NumericProperty

Builder.load_string("""
<Drs_Button>:
    canvas.before:
        Color:
            rgba: self.color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: 20, 20, 20, 20
        Color:
            rgba: 1, 1, 1, 1
        Line:
            rounded_rectangle: self.x, self.y, self.width, self.height, 20, 20, 20, 20
            width: 1.5
    Label: 
        pos_hint: {'x':0, 'y':0}
        size_hint: 1,1 
        text: 'DRS'
        color: root.color1
        
""")

class Drs_Button(FloatLayout):    
    drs_update = NumericProperty()
    color = ListProperty([0.043, 0.4, 0.13, 1])
    color1 = ColorProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(Drs_Button, self).__init__(**kwargs)
        self.bind(drs_update=self.update)

    def update(self, obj, val):
        if val:  
            self.color = [0.04, 0.6, 0.1, 1]
        else:
            self.color = [0, 0.6, 0, .2]
        

        