# importing libraries
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color, Canvas, Line
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty
from kivy.uix.image import Image
import math

Builder.load_string("""
<TrackMap>:   
    canvas:
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
        scalex = 2 * self.width / (maxx - minx) 
        scaley = 2.4 * self.height / (maxy - miny)
        for i in range(len(longs)):
            self.coords.append(self.y + scaley * (lats[i]-miny))
            self.coords.append(self.x + scalex * (longs[i]-minx))
            
# for converting geo_coords to x and y check this : https://stackoverflow.com/questions/16266809/convert-from-latitude-longitude-to-x-y
# and : https://en.wikipedia.org/wiki/Equirectangular_projection