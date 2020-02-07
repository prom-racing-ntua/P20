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
            xlabel: 'Time (mins)'
            ylabel: root.label
            x_grid: True
            x_grid_label: True
            y_grid: True
            y_grid_label: True
            y_ticks_major: 2
            x_ticks_major: 20
            xmin: 0
            xmax: 200 
            ymin: -10
            ymax: 10
        
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
    
    def __init__(self, **kwargs):
        super(Parametric_Graph, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[0,1,0,1])
        self.bind(update_graph= self.update)

    def update(self, *args):
        self.value += random.randint(-1, 1)
        self.time += 1
        self.points.append((self.time, self.value))
        self.plot.points = self.points
        self.mygraph.remove_plot(self.plot)
        self.mygraph.add_plot(self.plot) # this might add points indefenetly. should check if it crashes
        
        # possible fix 
        # self.my.graph.remove_plot(self.plot) # but it doesn't look that good.
