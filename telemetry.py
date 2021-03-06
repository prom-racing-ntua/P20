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
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
import random
import serial
import serial.tools.list_ports   # import serial module
import platform
import time
from datetime import datetime

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
from extractor import extract

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

#test
#f = open("log.txt", "r")

class MainScreen(App):

    ser_bytes = NumericProperty()
    ser = serial.Serial(baudrate=115200)
    data = ListProperty([0,0,0,0,0,0])
    info = ObjectProperty()
    errors = []
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

        #create data dictionary
        self.info = extract('telemetry2.xlsx')
        self.main.info = self.info
        self.diagnostics.info = self.info
        self.diagnostics.tabs.info = self.info 

        #Clock.schedule_interval(self.readserial, 0.05)
        Clock.schedule_interval(self.noserial, 0.5)
        return self.sm
    
    #keyboard inputs
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
        elif keycode == 273: #up
            if self.sm.current == 'diagnostics':
                if self.diagnostics.tabs.opacity == 0: # reset
                    self.diagnostics.rv.pos_hint = {"x": 0.02, "y": 0.02}
                    self.diagnostics.rv.size_hint = (0.7, 0.2)
                    self.diagnostics.tabs.pos_hint = {"x": 0.02, "y": 0.25}
                    self.diagnostics.tabs.size_hint = (0.7, 0.65)
                    self.diagnostics.tabs.opacity = 1
                else:
                    self.diagnostics.rv.pos_hint= {"x": 0.02, "y": 0.02}
                    self.diagnostics.rv.size_hint = (0.7, 0.05)
                    self.diagnostics.tabs.pos_hint = {"x": 0.02, "y": 0.08}
                    self.diagnostics.tabs.size_hint = (0.7, 0.9)
        elif keycode == 274: #down
            if self.sm.current == 'diagnostics':
                if self.diagnostics.tabs.size_hint[1] == 0.9: # reset
                    self.diagnostics.rv.pos_hint = {"x": 0.02, "y": 0.02}
                    self.diagnostics.rv.size_hint = (0.7, 0.2)
                    self.diagnostics.tabs.pos_hint = {"x": 0.02, "y": 0.25}
                    self.diagnostics.tabs.size_hint = (0.7, 0.65)
                else:
                    self.diagnostics.rv.pos_hint = {"x": 0.02, "y": 0.02}
                    self.diagnostics.rv.size_hint = (0.7, 0.95)
                    self.diagnostics.tabs.pos_hint = {"x": 0.02, "y": 0.06}
                    self.diagnostics.tabs.size_hint = (0.7, 0)
                    self.diagnostics.tabs.opacity = 0
        return True

    
    def readserial(self, dt):
        try:
            global ser
            if ser.in_waiting:
                #print(ser.in_waiting)
                #length = ser.in_waiting
                #temp = ser.readline()
                self.data = ser.readline().split()
                ser.reset_input_buffer()
                #print(len(self.data))
                #print(self.data[23])
                self.main.data = self.data
                #print(len(self.main.data))
                #print(str(int(self.data[28])))
                #self.diagnostics.data = self.data
                #self.data_screen.data = self.data
        except Exception as e:
            print(e)
            self.main.pc_status.serial_status = False
            try:
                ser = serial.Serial(
                    baudrate='115200',
                    timeout=1,
                    port=str(serial.tools.list_ports.comports()[0]).split()[0]
                    #port="/dev/ttyUSB0"
                )
                self.main.pc_status.serial_status = True
            except Exception:
                pass

    def noserial(self, dt):
        self.data = [random.randint(0,255) for i in range(60)] #instead of readserial

        #passes all the values 
        self.main.data = self.data
        self.diagnostics.update(self.data)
        #self.data_screen.data = self.data




    def update_errors2(self):
        self.errors = []
        for i in range(len(self.data)):
            self.errors.append(0)
        if int(self.data[7]) > 80:
            self.errors[7] = 2


    def update_errors(self):
        #stringA
        if self.data[0] == 0:
            for i in range(1,250):
                if self.data[i] > 250 or self.data[i] < 5:
                    self.errors.append({'datapos':i, 'value': self.data[i], 'timestamp': datetime.now().strftime("%H:%M:%S")})
        #stringB
        elif self.data[0] == 1:
            pass
        #stringC
        elif self.data[0] == 2:
            pass
        #log and remove the errors  if they bunch up
        if len(self.errors) > 20:
            self.errors = []

        
    

if __name__ == '__main__':
    try:
        MainScreen().run()
        
    except Exception as e:
        raise e
