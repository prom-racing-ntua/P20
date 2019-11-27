import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics', 'resizable', True)
from tire import Tire

class Tire_Temps(FloatLayout):
    def __init__(self, **kwargs):
        super(Tire_Temps, self).__init__(**kwargs)
        self.fl = Tire(pos_hint={"top": 1, "left": 1}, size_hint=(0.4, 0.45))
        self.fr = Tire(pos_hint={"top": 1, "right": 1}, size_hint=(0.4, 0.45))
        self.rl = Tire(pos_hint={"bottom": 1, "left": 1}, size_hint=(0.4, 0.45))
        self.rr = Tire(pos_hint={"bottom": 1, "right": 1}, size_hint=(0.4, 0.45))
        
        #arrow image
        #self.arrow = Image(source = "assets/arrow_vector.png")
        #self.arrow.size_hint_x = 0.7
        #self.arrow.size_hint_y = 0.7
        #self.arrow.pos_hint = {"x":0.15, "bottom":0.45}

        #self.add_widget(self.arrow)
        self.add_widget(self.fl)
        self.add_widget(self.fr)
        self.add_widget(self.rl)
        self.add_widget(self.rr)



