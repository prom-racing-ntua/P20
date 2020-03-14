#library imports
from kivy_garden.graph import Graph, MeshLinePlot, Plot
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import random

Builder.load_string("""
<Parametric_Graph>:
    mygraph: mygraph
    
    BoxLayout:
        size: root.size
        pos: root.pos 
        Graph:
            id: mygraph
            xlabel: 'Time(s)'
            ylabel: root.label
            x_grid: True
            x_grid_label: True
            y_grid: True
            y_grid_label: True
            y_ticks_major: root.boundaries[2]/6
            x_ticks_major: root.boundaries[1]/5
            xmin: root.boundaries[0]
            xmax: root.boundaries[1]
            ymin: root.boundaries[2]
            ymax: root.boundaries[3]
        
""")


class Parametric_Graph(BoxLayout):
    """A parametric graph of a given value in time \n
        Type:BoxLayout
    \n
    Parameters: \n
        boundaries: a list with upper and lower limits for both axis 
        label: name for the y-axis of the unit the graph represents
    """
    # passing arguments
    boundaries = ListProperty()
    label = StringProperty()
    # function arguments
    points = ListProperty()
    time = NumericProperty()
    mygraph = ObjectProperty()
    update_graph = ObjectProperty()
    plot = ObjectProperty()
    start_time = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Parametric_Graph, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[0,1,0,1])
        self.bind(update_graph= self.update)

    def update(self, obj, value):
        if not self.start_time:
            self.start_time = value[0]
        elif value[0] - self.start_time >= self.boundaries[1]:
            self.boundaries[1] *=2
        
        self.time = value[0] - self.start_time
        self.points.append([self.time, value[1] + 325])
        self.plot.points = self.points
        self.mygraph.remove_plot(self.plot)
        self.mygraph.add_plot(self.plot) 
        