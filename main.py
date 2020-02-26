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
from configparser import ConfigParser


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


class Main(Screen):
    
    data = ListProperty()
    
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)    
        config = ConfigParser()
        config.read('config.ini')
        cfgs = config['sensor_values']

        #setting up widgets
        self.tire_temps = Tire_Temps(pos_hint={"center_x": 0.5, "y": 0}, size_hint=(0.5, 0.3), temps=[[50, 50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50]], boundary=int(cfgs['infrared_offset']))
        self.battery = Parametric_Graph(pos_hint={"x":0, "y":0.32}, size_hint=(0.25, 0.5), label='Voltage (V)', boundaries=[0, 200, -10, 10])
        self.kw = Parametric_Bar(pos_hint={"x":0.02, "y":0.85}, size_hint=(0.05, 0.13), name="Power(kW)", value= 0, max_value=int(cfgs['kw_max']), color=[0,0,1,1], orientation="vertical")
        self.cur = Parametric_Bar(pos_hint={"x":0.09, "y":0.85}, size_hint=(0.05, 0.13), name="Current(A)", value=0, max_value=int(cfgs['cur_max']), color=[0,0,1,1], orientation="vertical")
        self.vol = Parametric_Bar(pos_hint={"x":0.16, "y":0.85}, size_hint=(0.05, 0.13), name="Voltage(V)", value=0, max_value=int(cfgs['vol_max']), color=[0,0,1,1], orientation="vertical")
        self.table = Time_Table(pos_hint = {'x':0.75,'y':0.5}, size_hint = (0.25,0.5))
        self.accel = Accel(pos_hint = {'center_x':0.5,'y':0}, size_hint = (0.2,0.3), acc=[50,50])
        self.map = TrackMap(pos_hint = {'x':0.82, 'y':0.05}, size_hint = (0.18, 0.3))
        self.pc_status = Pc_Status(pos_hint={"x":0.4, "y":0.85}, size_hint=(0.2, 0.15))
        self.apps = Parametric_Bar(pos_hint={"x":0.35, "y":0.65}, size_hint=(0.05, 0.13), name="APPS(%)", value=0, max_value=int(cfgs['apps_max']), color=[0,1,0,1], orientation="vertical")
        self.brake = Parametric_Bar(pos_hint={"x":0.42, "y":0.65}, size_hint=(0.05, 0.13), name="Brake(%)", value=0, max_value=int(cfgs['brake_max']), color=[1,0,0,1], orientation="vertical")
        self.bias = Brake_Bias(pos_hint={"x":0.35, "y":0.5}, size_hint=(0.1, 0.1), percentage = 0)
        self.rpmbar = RpmBar(pos_hint ={"x":0.35, "y":0.8},size_hint= (0.35, 0.05), value=1000, max_value=int(cfgs['rpm_max']), color=[1,0,0,1])
        self.motor_temp = Icon_Indicator(pos_hint={"x": 0.48, "y": 0.5}, size_hint=(0.1, 0.1), name="Motor Temp", value=0, unit="°C", boundaries=[int(cfgs['motor_temp_warn']), int(cfgs['motor_temp_crit'])], source="assets/gear.png", color=[1, 1, 1], opacity=0.7)
        self.inv_temp = Icon_Indicator(pos_hint={"x": 0.58, "y": 0.5}, size_hint=(0.1, 0.1), name="Inverter Temp", value=0, unit="°C", boundaries=[int(cfgs['inv_temp_warn']), int(cfgs['inv_temp_crit'])], source="assets/inverter2.png", color=[1, 1, 1, 1], opacity=0.4)
        self.bat_temp = Icon_Indicator(pos_hint={"x": 0.68, "y": 0.5}, size_hint=(0.1, 0.1), name="Battery Temp", value=0, unit="°C", boundaries=[int(cfgs['battery_temp_warn']), int(cfgs['battery_temp_crit'])], source="assets/battery4.png", color=[1, 1, 1, 1], opacity=0.6)
        self.gps_speed = Parametric_Label(pos_hint={"x":0.57, "y":0.65}, size_hint=(0.07, 0.1), name1="50", name2="GPS Speed", font1="32sp")
        self.hall_speed = Parametric_Label(pos_hint={"x":0.635, "y":0.65}, size_hint=(0.07, 0.1), name1="50", name2="Sensor Speed", font1="32sp")
        self.dashboard = Dashboard(pos_hint={"x":0.03, "y":0.05}, size_hint=(0.1, 0.2))
        self.drs_button = Drs_Button(pos_hint= {"x" : 0.5, "y": 0.65}, size_hint=(0.05, 0.05))
        self.steering_wheel = Icon_Indicator(pos_hint={"x": 0.48, "y": 0.35}, size_hint=(0.08, 0.08), name="Steering Angle", value=0, unit="°" , boundaries=[100,120], source="assets/steering_wheel2.png", color=[0.8,0.8,0.8,1], angle=0, opacity=1)
        
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
        self.add_widget(self.apps)
        self.add_widget(self.brake)
        self.add_widget(self.bias)
        self.add_widget(self.rpmbar)
        self.add_widget(self.motor_temp)
        self.add_widget(self.inv_temp)
        self.add_widget(self.bat_temp)
        self.add_widget(self.gps_speed)
        self.add_widget(self.hall_speed)
        self.add_widget(self.dashboard)
        self.add_widget(self.drs_button)
        self.add_widget(self.steering_wheel)

        #for testing
        
        self.bind(data=self.update)
        Clock.schedule_interval(self.tire_temps.update_linears, 0.05)
        Clock.schedule_interval(self.tire_temps.update_temps, 0.05)

    #for testing, steady
    def rpm(self, dt):
        if self.rpmbar.value > 9900:
            self.rpmbar.value = 1000
        self.rpmbar.value += 1000

    def update(self, obj, value):
        if self.data != []:
            self.steering_wheel.icon_update = int(self.data[4])
            self.motor_temp.value = int(self.data[3])
            self.battery.update_graph = [int(self.data[0])/1000, int(self.data[5])]
            self.inv_temp.value = int(self.data[6])
            self.bat_temp.value = int(self.data[7])
            self.kw.value = int(self.data[8])
            self.cur.value = int(self.data[9])
            self.vol.value = int(self.data[10])
            self.gps_speed.name1 = str(int(self.data[11]))
            self.hall_speed.name1 = str(int(self.data[12]))
            self.bias.percentage = int(self.data[13])
            self.apps.value = int(self.data[14])
            self.brake.value = int(self.data[15])
            self.rpmbar.value = int(self.data[16])