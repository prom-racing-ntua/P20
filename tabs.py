import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.graphics import Mesh

from tire_temps import Tire_Temps  # for test

Builder.load_string('''
<Tabs>:
    #pos_hint: self.pos_hint
    #size_hint: self.size_hint
    do_default_tab: False

    TabbedPanelItem:
        text: 'first tab'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'tab2'
        #Mesh:
            #mode: "triangle_fan"
            #vertices: [0,1,2]
            #indices: [0,1,2]
    TabbedPanelItem:
        text: 'Tire Temps'
        BoxLayout:
            #pos: self.pos
            #size: self.size    
            Tire_Temps:
                pos_hint: {"left":0, "top":0.85}
                size_hint: 0.4, 0.3

        
''')


class Tabs(TabbedPanel):
    def __init__(self, **kwargs):
        super(Tabs, self).__init__(**kwargs)
