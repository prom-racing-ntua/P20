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

class Main(Screen):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

        #setting up widgets
        self.tire_temps = Tire_Temps(pos_hint={"center_x": 0.5, "y": 0}, size_hint=(0.5, 0.3), temps=[[50, 50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50]])
        self.battery = Battery_Graph(pos_hint={"x":0, "y":0.32}, size_hint=(0.3, 0.5), points=[(600,0)])
        self.kw = Parametric_Bar(pos_hint={"x":0.02, "y":0.85}, size_hint=(0.05, 0.13), name="Power(kW)", value=50, max_value=100, color=[0,0,1,1], orientation="vertical")
        self.cur = Parametric_Bar(pos_hint={"x":0.09, "y":0.85}, size_hint=(0.05, 0.13), name="Current(A)", value=0, max_value=100, color=[0,0,1,1], orientation="vertical")
        self.vol = Parametric_Bar(pos_hint={"x":0.16, "y":0.85}, size_hint=(0.05, 0.13), name="Voltage(V)", value=100, max_value=100, color=[0,0,1,1], orientation="vertical")
        self.table = Time_Table(pos_hint = {'x':0.75,'y':0.5}, size_hint = (0.25,0.5))
        self.accel = Accel(pos_hint = {'center_x':0.5,'y':0}, size_hint = (0.2,0.3), acc=[50,50])
        self.map = TrackMap(pos_hint = {'x':0.85, 'y':0.2482}, size_hint = (0.2, 0.25))
        self.pc_status = Pc_Status(pos_hint={"x":0.4, "y":0.85}, size_hint=(0.2, 0.15))
        self.tps = Parametric_Bar(pos_hint={"x":0.35, "y":0.65}, size_hint=(0.05, 0.13), name="TPS(%)", value=30, max_value=100, color=[0,1,0,1], orientation="vertical")
        self.brake = Parametric_Bar(pos_hint={"x":0.42, "y":0.65}, size_hint=(0.05, 0.13), name="Brake(%)", value=5, max_value=100, color=[1,0,0,1], orientation="vertical")
        self.bias = Brake_Bias(pos_hint={"x":0.35, "y":0.5}, size_hint=(0.1, 0.1), percentage = 50)
        self.rpmbar = RpmBar(pos_hint ={"x":0.35, "y":0.8},size_hint= (0.35, 0.05), value=8500, max_value=10000, color=[1,0,0,1])
        self.motor_temp = Icon_Indicator(pos_hint={"x": 0.48, "y": 0.5}, size_hint=(0.1, 0.1), name="Motor Temp", value=50 , boundaries=[100,120], source="assets/gear.png", color=[1,1,1])
        self.inv_temp = Icon_Indicator(pos_hint={"x": 0.58, "y": 0.5}, size_hint=(0.1, 0.1), name="Inverter Temp", value=50 , boundaries=[100,120], source="assets/inv.png", color=[1,1,1])
        self.bat_temp = Icon_Indicator(pos_hint={"x": 0.68, "y": 0.5}, size_hint=(0.1, 0.1), name="Battery Temp", value=50 , boundaries=[100,120], source="assets/battery2.png", color=[1,1,1,0.1])
        self.gps_speed = Parametric_Label(pos_hint={"x":0.58, "y":0.65}, size_hint=(0.1, 0.13), name1="50", name2="GPS Speed", font1="32sp")
        self.hall_speed = Parametric_Label(pos_hint={"x":0.65, "y":0.65}, size_hint=(0.1, 0.13), name1="50", name2="Sensor Speed", font1="32sp")
        self.dashboard = Dashboard(pos_hint={"x":0.03, "y":0.05}, size_hint=(0.1, 0.2))
        #self.drs_button = Drs_Button(pos_hint= {"right" : 1, "y": 0.2}, size_hint=(0.05, 0.05))

        #adding widgets
        self.add_widget(self.battery)
        self.add_widget(self.tire_temps)
        self.add_widget(self.kw)
        self.add_widget(self.cur)
        self.add_widget(self.vol)
        self.add_widget(self.table)
        self.add_widget(self.accel)
        self.add_widget(self.map)
        self.add_widget(self.pc_status)
        self.add_widget(self.tps)
        self.add_widget(self.brake)
        self.add_widget(self.bias)
        self.add_widget(self.rpmbar)
        self.add_widget(self.motor_temp)
        self.add_widget(self.inv_temp)
        self.add_widget(self.bat_temp)
        self.add_widget(self.gps_speed)
        self.add_widget(self.hall_speed)
        self.add_widget(self.dashboard)
        #self.add_widget(self.drs_button)

        #for testing
        Clock.schedule_interval(self.acc_test, 0.2)
        Clock.schedule_interval(self.rpm, 0.05)
        #Clock.schedule_interval(self.)
 

    #for testing, steady
    def rpm(self, dt):
        if self.rpmbar.value > 9900:
            self.rpmbar.value = 1000
        self.rpmbar.value += 1000
        self.gps_speed.name1 = str(random.randint(0, 125))
        self.hall_speed.name1 = str(random.randint(0, 125))
        self.bias.percentage = random.randint(0, 100)

        
    #for testing, random
    def acc_test(self, dt):
        self.accel.acc = [self.accel.acc[0]+random.randint(-10,10), self.accel.acc[1]+random.randint(-10,10)]

    def dash_test(self, dt):
        #self.dashboard.status = [random.randint()]
        pass