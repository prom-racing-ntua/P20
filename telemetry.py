#library imports
from kivy.core.window import Window
import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, Canvas
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, NumericProperty
import random


#custom class imports
from left import Left
from middle import Middle
from right import Right

class MainScreen(App):
    data = ListProperty()
    timestamp = NumericProperty

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        #in order to launch maximized
        Window.fullscreen = 'auto'

        mainscreen = GridLayout()
        mainscreen.cols = 3

        self.timestamp = 0

        self.left = Left()
        self.middle = Middle()
        self.right = Right()

        self.data = [600,0]
        self.data = [600,0]

        mainscreen.add_widget(self.left)
        mainscreen.add_widget(self.middle)
        mainscreen.add_widget(self.right)

        #testing the backend
        #Clock.schedule_interval(self.get_data, 1)
        return mainscreen

    def get_data(self, dt):
        self.data[0]=self.data[0]-random.randint(0,5)
        self.data[1]+=1
        self.left.data[0]=self.data[0]
        self.left.data[1]=self.data[1]


if __name__ == '__main__':
    try:
        MainScreen().run()
    except Exception as e:
        raise e        
