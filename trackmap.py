# importing libraries
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color, Canvas, Line
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty
import math
from kivy.core.window import Window

Builder.load_string("""
<TrackMap>: 
    canvas:
        # Color:
        #     rgba: 1, 1, 1, 1
        # Line:
        #     rectangle: self.x,self.y,self.width,self.height
        #     width: 1.5
        Color:
            rgba: self.color
        Line:
            points: self.coords
            width: self.wid
       
""")

class TrackMap(RelativeLayout):

    coords = ListProperty([])
    color = ListProperty([1,1,0,1]) 
    wid = NumericProperty(3)       
    trackfile = ("./assets/track.txt")

    def __init__(self, **kwargs):
        super(TrackMap, self).__init__(**kwargs)
        earth_radius=6367116
        
        file = open(self.trackfile, "r")
        cosf0 = math.cos(math.radians(float(file.readline().split(',')[1]))) # used to approximate x and y coords to 1:1 aspect ratio
        longs=[]
        lats=[]
        for line in file:
            i = line.split(',')[0:2] 
            longs.append(earth_radius*math.radians(float(i[0])) * cosf0)
            lats.append(earth_radius*math.radians(float(i[1])))
        file.close()
        maxx = max(longs)
        minx = min(longs)
        maxy = max(lats)
        miny = min(lats)
        sizex = self.size_hint[0] * Window.width
        sizey = self.size_hint[1] * Window.height
        scalex = sizex / (maxx - minx)
        scaley = sizey / (maxy - miny)
        for i in range(len(longs)):
            self.coords.append(scaley * abs(lats[i]-miny))
            self.coords.append(scalex * abs(longs[i]-minx))
            
# for converting geo_coords to x and y check this : https://stackoverflow.com/questions/16266809/convert-from-latitude-longitude-to-x-y
# and : https://en.wikipedia.org/wiki/Equirectangular_projection