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
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
import random
import serial
import serial.tools.list_ports   # import serial module

#custom class imports
from tire_temps import Tire_Temps
from parametric_graph import Parametric_Graph
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
from drs_button import Drs_Button
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
    timestamp = NumericProperty
    data = ListProperty()    

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.fullscreen = 'auto'
        Main()
        Window.bind(on_key_down=self.press)
        self.timestamp = 0
        if comPorts != []:
            Clock.schedule_interval(self.readserial, 0.01)
        return sm

    def get_data(self, dt):
        self.data[0]=self.data[0]-random.randint(0,5)
        self.data[1]+=1
        self.left.data[0]=self.data[0]
        self.left.data[1]=self.data[1]
    
    def press(self, keyboard, keycode, text, modifiers, type):
        if keycode == 275: # ascii code for left
            if sm.current == 'main':
                sm.transition = SlideTransition(direction="left")
                sm.current = 'data'
            elif sm.current == 'diagnostics':
                sm.transition = SlideTransition(direction="left")
                sm.current = 'main'
        elif keycode == 276: # ascii code for right 
            if sm.current == 'main':
                sm.transition = SlideTransition(direction="right")
                sm.current = 'diagnostics'
            elif sm.current == 'data':
                sm.transition = SlideTransition(direction="right")
                sm.current = 'main'
        elif keycode == 27: # ascii code for ESC
            App.stop(self)
        return True
    
    def readserial(self, dt):
        if ser.in_waiting:
            temp = ser.readline()
            self.data = temp.split()
            print("Sender is running for:" , float(self.data[0])/1000, "seconds")

sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(Data_Screen(name='data'))
sm.add_widget(Diagnostics(name='diagnostics'))


if __name__ == '__main__':
    try:
        comPorts = list(serial.tools.list_ports.comports())
        if(comPorts != []):
            port_open = True
            ser = serial.Serial(
                port= 'COM3',
                baudrate= '115200', 
                timeout= 20 
            )
        
        MainScreen().run()
    except Exception as e:
        raise e
