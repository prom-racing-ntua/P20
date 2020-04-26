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

Builder.load_string("""
#:import Label kivy.uix.label.Label
<Datatabs>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width:1.25

    do_default_tab: False
""")


class Datatabs(TabbedPanel):

    lbls = ListProperty([])

    config = ConfigParser()
    config.read('config.ini')
    cfgs = config['diagnostics']

    def __init__(self, **kwargs):
        super(Datatabs, self).__init__(**kwargs)

        for key in self.cfgs:
            #temp = Label()
            #self.lbls.append()
            pass

        self.tractive = TabbedPanelHeader(text='Tractive System')
        #self.tractive.content = Label(text=self.lbls)
        #self.add_widget(self.tractive)

        Clock.schedule_once(self.test, 0.5)

    def test(self,dt):
        self.lbls = "new"
