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
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
import random
import serial
import serial.tools.list_ports   # import serial module
import platform

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
        size_hint: 0.035, 0.035
        pos_hint: {"right":1, "y":0}
        Button:
            size_hint: 1,1
            text: 'Data screen'
            on_press: 
                app.root.current = 'data'
                app.root.transition.direction = "left"
            
            font_size: 10
    BoxLayout:
        size_hint: 0.035, 0.035
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
        size_hint: 0.035, 0.035
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
        size_hint: 0.035, 0.035
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

    ser_bytes = NumericProperty()
    ser = serial.Serial()
    data = ListProperty([0,0,0,0,0,0])
    sm = ScreenManager()
    main = Main(name='main')
    data_screen = Data_Screen(name='data')
    diagnostics = Diagnostics(name='diagnostics')
    sm.add_widget(main)
    sm.add_widget(data_screen)
    sm.add_widget(diagnostics)

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.fullscreen = 'auto'
        Window.bind(on_key_down=self.press)
        #if serial.tools.list_ports.comports():
        Clock.schedule_interval(self.readserial, 0.01)
        return self.sm
    
    def press(self, keyboard, keycode, text, modifiers, type):
        if keycode == 275: # ascii code for left
            if self.sm.current == 'main':
                self.sm.transition = SlideTransition(direction="left")
                self.sm.current = 'data'
            elif self.sm.current == 'diagnostics':
                self.sm.transition = SlideTransition(direction="left")
                self.sm.current = 'main'
        elif keycode == 276: # ascii code for right 
            if self.sm.current == 'main':
                self.sm.transition = SlideTransition(direction="right")
                self.sm.current = 'diagnostics'
            elif self.sm.current == 'data':
                self.sm.transition = SlideTransition(direction="right")
                self.sm.current = 'main'
        elif keycode == 27: # ascii code for ESC
            App.stop(self)
        return True
    
    def readserial(self, dt):
        try:
            global ser
            if ser.in_waiting:
                temp = ser.readline()
                
                #print(ser.in_waiting)
                self.data = temp.split()
                self.main.data = self.data
                #print("Sender is running for:" , float(self.data[0])/1000, "seconds")
                self.diagnostics.data = self.data
                self.data_screen.data = self.data
                #print("Sender is running for:" , float(self.data[0])/1000, "seconds")
        except Exception as e:
            print(e)
            self.main.pc_status.serial_status = False
            try:
                ser = serial.Serial(
                    baudrate='115200',
                    timeout=20,
                    port=str(serial.tools.list_ports.comports()[0]).split()[0]
                )
                self.main.pc_status.serial_status = True
            except Exception:
                pass
    

if __name__ == '__main__':
    try:
        #if serial.tools.list_ports.comports():
            
            #ser = serial.Serial(
                #baudrate= '115200', 
                #timeout= 20,
                #port= str(serial.tools.list_ports.comports()[0]).split()[0]
            #)
        MainScreen().run()
        
    except Exception as e:
        raise e
