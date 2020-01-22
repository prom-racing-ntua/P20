# importing libraries
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color, Canvas, Line
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty
from kivy.uix.image import Image

Builder.load_string("""
<TrackMap>:
    canvas:
        Color:
            rgb: 0.05,0.05,0.05
        Rectangle:
            pos: self.pos
            size: self.size
            
        Line:
            rectangle: self.x, self.y, self.width, self.height
""")

class TrackMap(FloatLayout):

    trackfile = ("./assets/track.txt")    
    def __init__(self, **kwargs):
        super(TrackMap, self).__init__(**kwargs)
        longs = []
        lats = []
        file = open(self.trackfile, "r")
        
        for line in file:
            i = line.split(',')[0:2]
            longs.append(float(i[0]))
            lats.append(float(i[1]))
        
        file.close()
        maxx = max(lats)
        maxy = max(longs)
        minx = min(lats)
        miny = min(longs)
        scalex = 1.25 * (maxx - minx) # calculating a scale for x and y axis   
        scaley = 1.25 * (maxy - miny) # to project the distance between points in the scale
        # multiplying with 1.25 for the points to fit in the rectangle

        for longitude, latitude in zip(longs,lats):
            point = Image(pos_hint={"center_x": (latitude - minx) / scalex + 0.1, "center_y": (longitude - miny) / scaley + 0.1}, source="./assets/blue_dot.png", size_hint= (0.05, 0.05), opacity=1)
            self.add_widget(point)
