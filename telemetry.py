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
from kivy.uix.layout import Layout
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager
import random

#custom class imports
from tire_temps import Tire_Temps
from battery_graph import Battery_Graph
from parametric_bar import Parametric_Bar
from pc_status import Pc_Status
from rpmbar import RpmBar
from icon_indicator import Icon_Indicator
from parametric_label import Parametric_Label
from brake_bias import Brake_Bias
from accel import Accel
from time_table import Time_Table
from trackmap import TrackMap
from dashboard import Dashboard
from left import Left
from middle import Middle
from right import Right
#from drs_button import Drs_Button
from main import Main
from data_screen import Data_Screen
from diagnostics import Diagnostics

Builder.load_string("""
<Main>: 
    BoxLayout:
        size_hint: 0.05, 0.05
        pos_hint: {"right":1, "y":0}
        Button:
            size_hint: 1,1
            text: 'Data screen'
            on_press: 
                app.root.current = 'data'
                app.root.transition.direction = "left"
            
            font_size: 10
    BoxLayout:
        size_hint: 0.05, 0.05
        pos_hint: {"left":1, "y":0}
        Button:
            size_hint: 1,1
            text: 'Diagnostics'
            on_press: 
                app.root.current = 'diagnostics'
                app.root.transition.direction = "right"
            font_size: 10
            
<Data_Screen>:
    BoxLayout:
        size_hint: 0.05, 0.05
        pos_hint: {"left":1, "y":0}
        Button:
            size_hint: 1,1           
            text: 'Main Screen'
            on_press: 
                app.root.current = 'main'
                app.root.transition.direction = "right"
            font_size: 10
<Diagnostics>:
    BoxLayout:
        size_hint: 0.05, 0.05
        pos_hint: {"right":1, "y":0}
        Button:
            size_hint: 1,1
            text: 'Main Screen'
            on_press: 
                app.root.current = 'main'
                app.root.transition.direction = "left"
            font_size: 10

""")

class MainScreen(App):
    data = ListProperty()
    timestamp = NumericProperty

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        #in order to launch maximized
        Window.fullscreen = 'auto'
        Main()

        self.timestamp = 0

        #self.left = Left()
        #self.middle = Middle()
        #self.right = Right()

        #self.data = [600,0]
        #self.data = [600,0]

        #mainscreen.add_widget(self.left)
        #mainscreen.add_widget(self.middle)
        #mainscreen.add_widget(self.right)

        #testing the backend
        #Clock.schedule_interval(self.get_data, 1)
        return sm

    def get_data(self, dt):
        self.data[0]=self.data[0]-random.randint(0,5)
        self.data[1]+=1
        self.left.data[0]=self.data[0]
        self.left.data[1]=self.data[1]




sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(Data_Screen(name='data'))
sm.add_widget(Diagnostics(name='diagnostics'))


if __name__ == '__main__':
    try:
        MainScreen().run()
    except Exception as e:
        raise e
