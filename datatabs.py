#library imports
import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel,TabbedPanelHeader
from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty
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
    items = ObjectProperty({})
    info = ObjectProperty()

    #config = ConfigParser()
    #config.read('config.ini')
    #cfgs = config['sensor_values']



    def __init__(self, **kwargs):
        super(Datatabs, self).__init__(**kwargs)

        self.cols = 4
        #self.padding = 2

        #for i in self.info['by pos']:
            #print(i)
            #self.lbls.append(self.info[]
        #print(self.lbls)

        #for lbl in self.lbls:
            #self.items.append(Status_Label(label=lbl, data='0'))
            #self.add_widget(self.items[-1])

        self.bind(info=self.build_widget)

    def build_widget(self, obj, value):
        for i in self.info['by_pos']:
            self.lbls.append(self.info['by_pos'][i])
        for lbl in self.lbls:
            self.items[lbl] = Status_Label(label=lbl, data='0')
            self.add_widget(self.items[lbl])

