#library imports
import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel,TabbedPanelHeader
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from configparser import ConfigParser
from kivy.clock import Clock
from kivy.lang import Builder

#custom class imports
from status_label import Status_Label

Builder.load_string("""
#:import Label kivy.uix.label.Label
<Datatabs>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width:1.25
""")


class Datatabs(GridLayout):

    lbls = ListProperty([])
    items = ListProperty([])

    config = ConfigParser()
    config.read('config.ini')
    cfgs = config['sensor_values']

    def __init__(self, **kwargs):
        super(Datatabs, self).__init__(**kwargs)

        self.cols = 4
        #self.padding = 2

        self.lbls = self.cfgs['labels'].split(',')
        print(self.lbls)
        self.items = []

        for lbl in self.lbls:
            self.items.append(Status_Label(label=lbl, data='0'))
            self.add_widget(self.items[-1])



        #self.tractive = TabbedPanelHeader(text='Tractive System')
        #self.tractive.content = Label(text=self.lbls)
        #self.add_widget(self.tractive)
