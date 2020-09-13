# importing libraries
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color, Canvas, Line
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, ObjectProperty
import math
import random
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image

import utm

Builder.load_string("""
<TrackMap2>: 
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width:1.25  
        Color:
            rgba: 1,1,1,1
        Line:
            points: tuple(root.points)#tuple([(self.x+self.y+self.width*root.coordshint[i]) if i%2==0 else (self.x+self.y+self.height*root.coordshint[i]) for i in range(len(root.coordshint))])
            width: 2     
""")


class TrackMap2(FloatLayout):

    longs = ListProperty()
    lats = ListProperty()
    coordshint = ObjectProperty([])
    points = ObjectProperty([50,800,70,1000])
    coordstuple = ObjectProperty(())
    coords=ListProperty([])
    color = ListProperty([1, 1, 0, 1])
    wid = NumericProperty(3)
    trackfile = ("./assets/track.txt")
    im = Image()
    index = NumericProperty(0)

    def __init__(self, **kwargs):
        super(TrackMap2, self).__init__(**kwargs)
        earth_radius = 6367116
        #print(self.pos,self.size)

        file = open(self.trackfile, "r")
        # used to approximate x and y coords to 1:1 aspect ratio
        f=1
        maxx=0
        minx=0
        maxy=0
        miny=0
        c=0
        for line in file:
            i = line.split(',')[0:2]
            self.coords.append(list(utm.from_latlon(float(i[1]), float(i[0]))))
            #print(self.coords)
            #print(list(utm.from_latlon(float(i[1]), float(i[0]))))
            try:
                if f:
                    maxx = self.coords[0][0]
                    minx = self.coords[0][0]
                    maxy = self.coords[0][1]
                    miny = self.coords[0][1]
                    f = 0
            
                if self.coords[c][0]>maxx:
                    maxx=self.coords[c][0]
                if self.coords[c][0]<minx:
                    minx=self.coords[c][0]
                if self.coords[c][1]>maxy:
                    maxy=self.coords[c][1]
                if self.coords[c][1]<miny:
                    miny=self.coords[c][1]
                c+=1
            except Exception as e:
                print(e)
        file.close()

        #print(self.canvas.before.x)
        for i in self.coords:
            self.coordshint.append((i[0] - minx)/(maxx - minx))
            self.coordshint.append((i[1] - miny)/(maxy - miny))
        self.coordstuple=tuple(self.coordshint)
        #print(self.coordshint)
        #print(self.coordshint)

        Clock.schedule_once(self.render,0.1)
        #print(Window.height, Window.width)
        #print(self.width,self.height)
        #print(self.x,self.y)

        

    def render(self,dt):
        self.points = [(self.pos[0]+self.width*self.coordshint[i]) if i % 2 == 0 else (
            self.pos[1]+self.height*self.coordshint[i]) for i in range(len(self.coordshint))]
        #print(self.points)
        self.canvas.add(Line(points=self.points, width=1))
