# importing libraries
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color, Canvas, Line
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty
import math
import random
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image

Builder.load_string("""
<TrackMap>: 
    canvas.before:
        Color:
            rgba: self.color
        Line:
            points: self.coords
            width: self.wid

       
""")

class TrackMap(RelativeLayout):

    longs = ListProperty()
    lats = ListProperty()
    coords = ListProperty([])
    color = ListProperty([1,1,0,1]) 
    wid = NumericProperty(3)       
    trackfile = ("./assets/track.txt")
    im = Image()
    def __init__(self, **kwargs):
        super(TrackMap, self).__init__(**kwargs)
        earth_radius=6367116
        
        file = open(self.trackfile, "r")
        cosf0 = math.cos(math.radians(float(file.readline().split(',')[1]))) # used to approximate x and y coords to 1:1 aspect ratio
        for line in file:
            i = line.split(',')[0:2] 
            self.longs.append(earth_radius*math.radians(float(i[0])) * cosf0)
            self.lats.append(earth_radius*math.radians(float(i[1])))
        file.close()

        Clock.schedule_once(self.after_init)
        Clock.schedule_interval(self.update_track_position, 1)

    def after_init(self, dt):
        maxx = max(self.longs)
        minx = min(self.longs)
        maxy = max(self.lats)
        miny = min(self.lats)
        pixel_height = 1.2 * self.size_hint[1] * 600 
        pixel_width = self.size_hint[0] * 800
        #print(Window.height, Window.width) 
        scalex = pixel_width / (maxx - minx)
        scaley = pixel_height / (maxy - miny)
        for i in range(len(self.longs)):
            self.coords.append(scaley * abs(self.lats[i]-miny))
            self.coords.append(scalex * abs(self.longs[i]-minx))

    def update_track_position(self, dt):
        self.remove_widget(self.im)
        index = random.randint(0,len(self.coords))
        if index%2:
            index-=1
        self.im = Image(pos=(self.coords[index], self.coords[index+1]), source="assets/red_dot.png", size_hint= (0.05, 0.05), opacity=1)
        self.add_widget(self.im)
            
# for converting geo_coords to x and y check this : https://stackoverflow.com/questions/16266809/convert-from-latitude-longitude-to-x-y
# and : https://en.wikipedia.org/wiki/Equirectangular_projection
