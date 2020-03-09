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
            xlabel: 'Time (secs)'
            ylabel: root.label
            x_grid: True
            x_grid_label: True
            y_grid: True
            y_grid_label: True
            y_ticks_major: 40
            x_ticks_major: root.xmax/10
            xmin: 0
            xmax: root.xmax
            ymin: 300
            ymax: 588
        
""")


class Parametric_Graph(BoxLayout):
    points = ListProperty()
    value = NumericProperty()
    time = NumericProperty()
    label = StringProperty()
    mygraph = ObjectProperty()
    update_graph = ObjectProperty()
    plot = ObjectProperty()
    boundaries = ListProperty()
    xmax = NumericProperty(10)
    start_time = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Parametric_Graph, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[0,1,0,1])
        self.bind(update_graph= self.update)

    def update(self, obj, value):
        if value[0] - self.start_time >= self.xmax:
            self.xmax *=2

        self.value = value[1]
        if self.start_time == 0:
            self.start_time = value[0]
        self.time = value[0] - self.start_time
        #print(self.time)
        self.points.append([self.time, self.value + 325])
        self.plot.points = self.points
        self.mygraph.remove_plot(self.plot)
        self.mygraph.add_plot(self.plot) 
        