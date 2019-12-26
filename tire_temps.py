#library imports
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
from kivy.clock import Clock

#custom class imports
from tire import Tire
from flashing_arrows import Flashing_Arrows

class Tire_Temps(FloatLayout):
    def __init__(self, **kwargs):
        super(Tire_Temps, self).__init__(**kwargs)
        self.desc = Label(text="Tire Temps", pos_hint={"x": 0.4, "y": 0.9}, size_hint=(0.2, 0.1))
        self.fl = Tire(pos_hint={"x": 0, "y": 0.5}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.fr = Tire(pos_hint={"x": 0.6, "y": 0.5}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.rl = Tire(pos_hint={"x": 0, "y": 0}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.rr = Tire(pos_hint={"x": 0.6, "y": 0}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        
        self.arr = Flashing_Arrows(pos_hint={"x": 0.45, "y": 0}, size_hint=(0.1, 0.9))
        
        self.add_widget(self.desc)
        self.add_widget(self.fl)
        self.add_widget(self.fr)
        self.add_widget(self.rl)
        self.add_widget(self.rr)
        
        self.add_widget(self.arr)

        Clock.schedule_interval(self.update, 0.5)

    def update(self, dt):
        for i in range(4):
            self.fl.temp[i] += 1



