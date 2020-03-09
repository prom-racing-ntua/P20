#library imports
from kivy_garden.graph import Graph, MeshStemPlot, Plot, MeshLinePlot
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import random
from operator import itemgetter

Builder.load_string("""
<Histogram>:
    mygraph: mygraph
    
    BoxLayout:
        size: root.size
        pos: root.pos 
        Graph:
            id: mygraph
            xlabel: root.label
            ylabel: "Frequency"
            x_grid: True
            x_grid_label: True
            y_grid: True
            y_grid_label: True
            y_ticks_major: root.ymax / 5
            x_ticks_major: 20
            ymin: 0
            ymax: root.ymax
            xmin: 300
            xmax: 588
        
""")


class Histogram(BoxLayout):
    points = ListProperty()
    value = NumericProperty()
    time = NumericProperty()
    label = StringProperty()
    mygraph = ObjectProperty()
    update_graph = ObjectProperty()
    plot = ObjectProperty()
    boundaries = ListProperty()
    ymax = NumericProperty(10)
    freq = ListProperty()

    def __init__(self, **kwargs):
        super(Histogram, self).__init__(**kwargs)
        self.plot = MeshStemPlot(color=[0,1,0,1])
        self.bind(update_graph= self.update)
        self.freq = [0]*288
        
    def update(self, obj, value):
        if(max(self.freq) >= self.ymax):
            self.ymax *=2
        self.value = value
        for i in range(300, 588, 5):
            if(self.value - i + 300<=5):
                self.value = i
        self.freq[self.value-300]+=1
        self.points.append([self.value,self.freq[self.value - 300]])
        self.points.append([self.value+0.01, 0])
        self.plot.points = sorted(self.points, key= itemgetter(0))
        self.mygraph.remove_plot(self.plot)
        self.mygraph.add_plot(self.plot) 
        