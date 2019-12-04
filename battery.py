import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock

from segment import Segment

Builder.load_string('''
<Battery>:
    seg: seg
    lbl: lbl
    Label:
        id: lbl
        text: "Battery Status"
        pos_hint: {"x": 0, "y": 0.9} 
        size_hint: 0.6, 0.1
    BoxLayout:
        id: seg
        orientation: "horizontal"
        pos_hint: {"x": 0, "y": 0}
        size_hint: 1, 0.75
        canvas:
            Color:
                rgba: 0,1,0,1
            Line:
                rectangle: self.x,self.y,self.width,self.height
                width: 1.25

''')

class Battery(FloatLayout):
    segment = ListProperty()
    seg = ObjectProperty()
    lbl = ObjectProperty()

    def __init__(self, **kwargs):
        super(Battery, self).__init__(**kwargs)
        #self.seg.add_widget(Label(text="smt"))
        #self.seg = BoxLayout()
        #self.add_widget(self.seg)
        print(self.children)
        #for i in range(7):
            #self.seg.add_widget(Label(text=str(i)))
            #self.segment.append(Segment(seg_id=str(i), voltage=50, temp=40))
            #self.battery.add_widget(self.segment[i])
            #print("added new segment")
        #add misc labels
        Clock.schedule_once(self._after_init, 0.1)

    def _after_init(self, dt):
        print(self.seg)
        print(self.lbl.text)
        new_bat = self.seg
        for i in range(7):
            new_seg = Segment(seg_id=str(i), voltage=50, temp=40)
            new_bat.add_widget(new_seg)
            print("added new segment")
        self.seg = new_bat 

