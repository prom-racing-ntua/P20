#library imports
import kivy
from kivy.lang import Builder
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import random

#custom library imports
from grid import Grid

Builder.load_string('''
<Dashboard>:        
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: root.x, root.y, root.width , root.height
    Label:
        text: "Shutdown"
        pos_hint: {"x":0.4, "y":0.93}
        size_hint: 0.2, 0.05
        font_size: "20sp"
    Label:
        text: "Status"
        pos_hint: {"x":0.4, "y":0.6}
        size_hint: 0.2, 0.05
        font_size: "20sp"
    Label:
        text: "Buttons"
        pos_hint: {"x":0.4, "y":0.27}
        size_hint: 0.2, 0.05
        font_size: "20sp"
    
''')

class Dashboard(FloatLayout):

    status = ListProperty([255,255,255,255])
    shutdown_labels = ["AMS","IMD","BSPD"]
    airs_labels = ["Air-", "Air+"]
    button_labels = ["A/A", "RTD", "DRS", "Page Left", "Page Right", "Encoder"]
    status_labels = ["A/A", "RTD", "VCU Req", "Inverter Enable", "DRS"]
    
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        #byte0 = random.randint(0,255)
        #byte0 = 6
        #for i in range(3):
        #    self.bstatus.append(byte0 & 1 << i !=0)

        #print(self.bstatus)

        self.shutdown = Grid(size_hint= (0.8,0.22), pos_hint= {"x": 0, "y": 0.68}, labels= self.shutdown_labels, colors = [1,1,1])
        self.airs = Grid(size_hint= (0.2,0.22), pos_hint= {"x": 0.8, "y": 0.68}, labels= self.airs_labels, colors = [0,0])
        self.buttons = Grid(size_hint= (1,0.22), pos_hint= {"x":0, "y": 0}, labels= self.button_labels, colors = [2,2,2,2,2,2])
        self.statuses = Grid(size_hint= (1,0.22), pos_hint= {"x":0, "y": 0.35}, labels= self.status_labels, colors = [0,0,0,0,0])

        self.add_widget(self.shutdown)
        self.add_widget(self.airs)
        self.add_widget(self.buttons)
        self.add_widget(self.statuses)

        #self.ams = Status_Led(size_hint=(0.1, 0.3), pos_hint={"x": 0.3, "y": 0.3}, label = "AMS", status=1)
        #self.add_widget(self.ams)

        self.bind(status=self.update)
        #self.shutdown.status = [1,0,1]

    def update(self, obj, value):
        #print(self.status)
        shut = [self.status[0] >> 0 & 1, self.status[0] >> 1 & 1, self.status[0] >> 2 & 1]
        air = [not (self.status[0] >> 3 & 1), not (self.status[0] >> 4 & 1)]
        stat = [self.status[0] >> 5 & 1, self.status[0] >> 6 & 1, self.status[1] >> 0 & 1, 0, self.status[0] >> 7 & 1]
        btns = [self.status[1] >> 2 & 1, self.status[1] >> 3 & 1, self.status[1] >> 7 & 1, self.status[1] >> 5 & 1, self.status[1] >> 6 & 1, self.status[1] >> 4 & 1]
        self.shutdown.status = shut
        self.airs.status = air
        self.statuses.status = stat
        self.buttons.status = btns