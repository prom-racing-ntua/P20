#library imports
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock

#custom library imports


Builder.load_string('''
<Grid>:
    rows: 2
    cols: len(root.labels)
        
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: root.x, root.y, root.width , root.height
    
''')


class Grid(GridLayout):

    labels = ListProperty()
    status = NumericProperty(255)

    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.padding = 10
        
        for i in range(len(self.labels)): 
            self.add_widget(Label(text =self.labels[i]))
            
        for i in range(len(self.labels)): 
            self.add_widget(Image(source ="assets/green_dot.png", size_hint = (0.35, 0.35)))
        
        self.bind(status= self.update)


    def update(self, obj, value):
        for i in range(len(self.labels)): 
            if self.value & 2**i:
                self.add_widget(Image(source ="assets/green_dot.png", size_hint = (0.35, 0.35)))
            else:
                self.add_widget(Image(source ="assets/red_dot.png", size_hint = (0.35, 0.35)))
