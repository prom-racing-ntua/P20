import kivy
kivy.require('1.10.1')
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.properties import StringProperty, ListProperty, NumericProperty

cl = [[1, 0, 0], [1, 0.36, 0], [1, 0.73, 0], 
    [0.91, 1, 0], [0.55, 1, 0], 
    [0.18, 1, 0], [0, 1, 0.18], 
    [0, 1, 0.55], [0, 1, 0.91], 
    [0, 0.73, 1], [0, 0.36, 1], [0, 0, 1]]


Builder.load_string('''
<Tire>:
    name: self.name
    orientation: "horizontal"
    Label:
        text: str(root.temp[0])
        canvas.before:
            Color:
                rgb: root.colors[0]
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [20,0,0,20]
            Color:
                rgba: 1,1,1,0.8
            Line:
                rounded_rectangle: self.x, self.y, self.width, self.height, 20, 0, 0, 20
                width: 1.25
    Label:
        text: str(root.temp[1])
        canvas.before:
            Color:
                rgb: root.colors[1]
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [0,0,0,0]
            Color:
                rgba: 1,1,1,0.8
            Line:
                rectangle: self.x,self.y,self.width,self.height
                width: 1.25
    Label:
        text: str(root.temp[2])
        canvas.before:
            Color:
                rgb: root.colors[2]
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [0,0,0,0]
            Color:
                rgba: 1,1,1,0.8
            Line:
                rectangle: self.x,self.y,self.width,self.height
                width: 1.25
    Label:
        text: str(root.temp[3])
        canvas.before:
            Color:
                rgb: root.colors[3]
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [0,20,20,0]
            Color:
                rgba: 1,1,1,0.8
            Line:
                rounded_rectangle: self.x, self.y, self.width, self.height, 0, 20, 20, 0
                width: 1.25
''')

class Tire(BoxLayout):
    name = StringProperty()
    temp = ListProperty()
    colors = ListProperty(defaultvalue = [[0,0,1], [0,0,1], [0,0,1], [0,0,1]]) 

    def __init__(self,x=None,y=None, **kwargs):
        super(Tire, self).__init__(**kwargs)

        self.bind(temp=self.color_picker)

    def color_picker(self, obj, value):
        for i in range(4):
            self.colors[i] = cl[round((150-self.temp[i])/12)]
        


