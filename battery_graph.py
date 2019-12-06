#library imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.boxlayout import BoxLayout

class Battery_Graph(Graph, BoxLayout):
    points = ListProperty()

    def __init__(self, **kwargs):
        super(Battery_Graph, self).__init__(**kwargs)
        self.graph = Graph(xlabel='Time', ylabel='Voltage',
                           x_ticks_major=10, y_ticks_major=50,
                           y_grid_label=True, x_grid_label=True, padding=5,
                           x_grid=True, y_grid=True, xmin=0, xmax=50, ymin=300, ymax=600)
        self.plot = MeshLinePlot(color=[0,1,0,1])
        self.plot.points = self.points
        self.graph.add_plot(self.plot)
        print(self.points)
        self.add_widget(self.graph)


        
