#library imports
import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock

#custom library imports


Builder.load_string('''
<Dashboard>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 1
    Label:
        text: root.dash_labels[0]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 2
    Label:
        text: root.dash_labels[1]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 4
    Label:
        text: root.dash_labels[2]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 8
    Label:
        text: root.dash_labels[3]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 16
    Label:
        text: root.dash_labels[4]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 32
    Label:
        text: root.dash_labels[5]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 64
    Label:
        text: root.dash_labels[6]
    Image:
        source: "assets/green_dot.png"
        size_hint: 0.05, 0.05        
        opacity: root.status & 128
    Label:
        text: root.dash_labels[7] 
    
''')


class Dashboard(GridLayout):

    status = NumericProperty(255)
    dash_labels = ["BMS","IMD","TS Active", "A/A status", "A/A button",
    "RTD status", "RTD button", "Shutdown"]

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.cols = 4
        self.padding = 10
        

