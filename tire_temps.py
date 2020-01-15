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
from kivy.properties import ListProperty, NumericProperty
import random

#custom class imports
from tire import Tire
#from flashing_arrows import Flashing_Arrows
from progress_bar import Progress_Bar


class Tire_Temps(FloatLayout):
    """A widget outlining tire temperatures and linear sensor values representing suspension travel \n
        Type:FloatLayout
        Uses Progress_Bar and Tire class 
    \n
    Parameters: \n
        \n 
    Update Functionality:

    """

    temps = ListProperty()
    lin = ListProperty()
    def __init__(self, **kwargs):
        
        super(Tire_Temps, self).__init__(**kwargs)
        #self.desc = Label(text="Tire Temps", pos_hint={"x": 0.4, "y": 0.9}, size_hint=(0.2, 0.1))
        self.fl = Tire(pos_hint={"x": 0, "y": 0.5}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.fr = Tire(pos_hint={"x": 0.6, "y": 0.5}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.rl = Tire(pos_hint={"x": 0, "y": 0}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.rr = Tire(pos_hint={"x": 0.6, "y": 0}, size_hint=(0.4, 0.47), temp = [50,50,50,50])
        self.fll = Progress_Bar(pos_hint={"x": 0.42, "y": 0.5}, size_hint=(0.05, 0.47) , orientation="vertical", color=[0,0,1,1], active_blocks=5)
        self.frl = Progress_Bar(pos_hint={"x": 0.52, "y": 0.5}, size_hint=(0.05, 0.47) , orientation="vertical", color=[0,0,1,1], active_blocks=5)
        self.rll = Progress_Bar(pos_hint={"x": 0.42, "y": 0}, size_hint=(0.05, 0.47) , orientation="vertical", color=[0,0,1,1], active_blocks=5)
        self.rrl = Progress_Bar(pos_hint={"x": 0.52, "y": 0}, size_hint=(0.05, 0.47) , orientation="vertical", color=[0,0,1,1], active_blocks=5)
        
        #self.arr = Flashing_Arrows(pos_hint={"x": 0.45, "y": 0}, size_hint=(0.1, 0.9))
        
        #self.add_widget(self.desc)
        self.add_widget(self.fl)
        self.add_widget(self.fr)
        self.add_widget(self.rl)
        self.add_widget(self.rr)
        self.add_widget(self.fll)
        self.add_widget(self.frl)
        self.add_widget(self.rll)
        self.add_widget(self.rrl)
        
        #self.add_widget(self.arr)

        Clock.schedule_interval(self.update, 0.5)
        Clock.schedule_interval(self.update_temps, 0.5)
        Clock.schedule_interval(self.update_linears, 0.1)

        self.bind(temps=self.update_temps)

    def update(self, dt):
        for i in range(4):
            self.temps[0][i] += 1
            self.temps[1][i] += 1
            self.temps[2][i] += 1
            self.temps[3][i] += 1
    
    def update_temps(self, dt):
        for i in range(4):
            self.fl.temp[i] = self.temps[0][i]
            self.fr.temp[i] = self.temps[1][i]
            self.rl.temp[i] = self.temps[2][i]
            self.rr.temp[i] = self.temps[3][i]
        
    def update_linears(self, dt):
        self.fll.active_blocks = random.randint(0,19)
        self.frl.active_blocks = random.randint(0,19)
        self.rll.active_blocks = random.randint(0,19)
        self.rrl.active_blocks = random.randint(0,19)



