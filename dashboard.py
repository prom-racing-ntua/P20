#library imports
import kivy
from kivy.lang import Builder
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

#custom library imports
from grid import Grid

class Dashboard(FloatLayout):

    status = NumericProperty(255)
    shutdown_labels = ["AMS","IMD","BSPD", "A/A Relay"]
    button_labels = ["A/A", "RTD", "DRS", "Page Left", "Page Right", "Encoder"]
    status_labels = ["A/A", "RTD", "VCU Req", "VCU OK", "DRD", "Inverter Enable"]
    
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        shutdown = Grid(size_hint= (self.size_hint[0] / 1.5, self.size_hint[1]), pos_hint= {"x":self.pos_hint["x"], "y": 14 * self.pos_hint["y"]}, labels= self.shutdown_labels)
        buttons = Grid(size_hint= self.size_hint, pos_hint= {"x":self.pos_hint["x"], "y": 7.5 * self.pos_hint["y"]}, labels= self.button_labels)
        status = Grid(size_hint= self.size_hint, pos_hint= {"x":self.pos_hint["x"], "y": self.pos_hint["y"]}, labels= self.status_labels)

        self.add_widget(shutdown)
        self.add_widget(buttons)
        self.add_widget(status)

        self.bind(status= self.update)

    def update(self, obj, value):
        #self.shutdown.status = self.status
        pass