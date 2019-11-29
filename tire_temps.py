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
from flashing_arrows import Flashing_Arrows

class Tire_Temps(FloatLayout):
    def __init__(self, **kwargs):
        super(Tire_Temps, self).__init__(**kwargs)
        print(self.pos_hint, self.size_hint)
        self.fl = Tire(pos_hint={"x": 0, "y": 0.55}, size_hint=(0.45, 0.45))
        self.fr = Tire(pos_hint={"x": 0.55, "y": 0.55}, size_hint=(0.45, 0.45))
        self.rl = Tire(pos_hint={"x": 0, "y": 0}, size_hint=(0.45, 0.45))
        self.rr = Tire(pos_hint={"x": 0.55, "y": 0}, size_hint=(0.45, 0.45))
        
        self.arr = Flashing_Arrows(pos_hint={"x": 0.45, "y": 0}, size_hint=(0.1, 1))

        self.add_widget(self.fl)
        self.add_widget(self.fr)
        self.add_widget(self.rl)
        self.add_widget(self.rr)
        
        self.add_widget(self.arr)



