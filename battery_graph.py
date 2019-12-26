#library imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

class Battery_Graph(BoxLayout):
    points = ListProperty()
    cur = NumericProperty()
    mins = NumericProperty()

    def __init__(self, **kwargs):
        super(Battery_Graph, self).__init__(**kwargs)
        self.graph = Graph(xlabel='Time(mins)', ylabel='Voltage(V)',
                           x_ticks_major=10, y_ticks_major=50,
                           y_grid_label=True, x_grid_label=True,
                           x_grid=True, y_grid=True, xmin=0, xmax=50, ymin=300, ymax=600)
        self.plot = MeshLinePlot(color=[0,1,0,1])
        self.plot.points = self.points
        self.graph.add_plot(self.plot)
        self.add_widget(self.graph)
        #self.plot.bind_to_graph(self.graph)
        self.cur = 600
        self.mins = 0

        #self.bind(points=self._update)
        #Clock.schedule_interval(self._update,1)
    
    def _update(self, *args):
        #print(self.points[0][0])
        self.cur += random.randint(-10, -1)
        self.mins += 1
        self.points.append((self.cur,self.mins))
        print(self.points)
        #self.plot.points = self.points
        #print(self.plot.points)
        self.graph.remove_plot(self.plot)
        self.plot = MeshLinePlot(color=[0,1,0,1])
        self.plot.points = self.points
        self.graph.add_plot(self.plot)


        
