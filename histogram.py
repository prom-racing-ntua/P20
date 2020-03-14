#library imports
from kivy_garden.graph import Graph, MeshStemPlot
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
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
            y_ticks_major: root.boundaries[3] / 5
            x_ticks_major: root.boundaries[0] / root.histogram_points
            xmin: root.boundaries[0]
            xmax: root.boundaries[1]
            ymin: root.boundaries[2]
            ymax: root.boundaries[3]
        
""")

class Histogram(BoxLayout):
    # passing arguments
    label = StringProperty()
    boundaries = ListProperty()
    histogram_points = NumericProperty()
    # function arguments
    points = ListProperty()
    mygraph = ObjectProperty()
    update_graph = ObjectProperty()
    plot = ObjectProperty()
    freq = ListProperty()

    def __init__(self, **kwargs):
        super(Histogram, self).__init__(**kwargs)
        self.plot = MeshStemPlot(color=[0,1,0,1])
        self.bind(update_graph= self.update)
        self.freq = [0]*288


    def update(self, obj, value):
        if(max(self.freq) >= self.boundaries[3]):
            self.boundaries[3] *=2
        for i in range(300, 588, self.histogram_points):
            if(value - i + 300 <= self.histogram_points):
                value = i
        self.freq[value-300]+=1
        self.points.append([value,self.freq[value - 300]])
        self.points.append([value + 0.01, 0])
        self.plot.points = sorted(self.points, key= itemgetter(0))
        self.mygraph.remove_plot(self.plot)
        self.mygraph.add_plot(self.plot) 
        