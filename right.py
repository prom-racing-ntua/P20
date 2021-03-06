#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
import random


#custom class imports
from accel import Accel
from time_table import Time_Table
from trackmap import TrackMap

class Right(FloatLayout):
    def __init__(self, **kwargs):
        super(Right, self).__init__(**kwargs)
        self.table = Time_Table(pos_hint = {'x':0,'y':0.5}, size_hint = (1,0.5))
        self.accel = Accel(pos_hint = {'x':0.6,'y':0.25}, size_hint = (0.4,0.25), acc=[50,50])
        self.add_widget(self.table)
        self.add_widget(self.accel)
        self.map = TrackMap(pos_hint = {'x':0.099, 'y':0.2482}, size_hint = (0.5, 0.25))
        self.add_widget(self.map)
        #for testing
        Clock.schedule_interval(self.acc_test, 0.2)

    #for testing, random
    def acc_test(self, dt):
        self.accel.acc = [self.accel.acc[0]+random.randint(-10,10), self.accel.acc[1]+random.randint(-10,10)]



