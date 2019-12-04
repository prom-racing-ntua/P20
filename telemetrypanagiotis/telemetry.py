#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.10.0')
from kivy.config import Config
Config.set('graphics', 'width', str(1200))
Config.set('graphics', 'height', str(700))
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line,Color
from kivy.uix.image import Image
from kivy.garden.graph import LinePlot, MeshLinePlot
from customGraph import Graph
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.slider import Slider
from datetime import datetime
import time,math,random,numpy
import Queue as queue
from collections import deque
from datetime import *
from landingForm import LandingForm
from popupwidget import PopupWidget


from test import TestWidget
from sectors import Sectors
from center import *
#from left import *
from right import *
#import serial

RR_lin = 178
RL_lin = 179
FR_lin = 197
FL_lin = 194

streamlineA = list()
for i in range(23):
	streamlineA.append(0)


streamlineB = list()
for i in range(23):
	streamlineB.append(0)

streamlineC = list()
for i in range(23):
	streamlineC.append(0)




def convert(clat,clon):    ##convert gps coords
	# 3804.1712,02348.9058
	lat=int(clat[0:2])+round(float(clat[2:9])/60,6)
	lon=int(clon[0:3])+round(float(clon[3:10])/60,6)
	return lat,lon

file = open("/home/panos/teelemtry_dimos/track.txt", "r")
temp = []
j=0
for line in file:
	temp.append((float(line.split(',')[0]),float(line.split(',')[1])))
start_time=0
i=0
if __name__ == '__main__':
	#ser = serial.Serial('/dev/ttyS2',115200)
	# ser = serial.Serial('/dev/ttyACM0',115200)  ##(for linux)
	while(1):
		try:
			mydata = str(ser.readline()).split("'")[1].split('\\')[0].split(',')
			if	len(mydata)==23:
				start_time=int(mydata[0])
				break
			print(mydata)
		except Exception as e:
			print("FAILED")

	class TelemetryApp(App):
		i = 0
		def build(self):
			Window.clearcolor = (0,0,0,1)
			Window.fullscreen = False
			main_window=FloatLayout()
			main_window.add_widget(left_column)
			main_window.add_widget(center_column)
			main_window.add_widget(right_column)

			# popup = Popup(
			# 		title='Telemetry Setup',
			# 		content = PopupWidget(),
			# 		confirm = Button(text = 'confirm',pos_hint={'x':0.5,'y':0.15}),
			# 		pos_hint={'x':0.20,'y':0.1},
			# 		size_hint=(0.6, 0.8))
			# confirm.bind(on_press= popup.dismiss)
			# main_window.add_widget(popup)
			# print (popup.content.children)
			# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			Clock.schedule_interval(lambda *t: self.get_data(), 0.02)
			return main_window
		def get_data(self):
			global start_time ,streamlineA,streamlineB,streamlineC,i
			if ser.in_waiting:
				try:
					mydata = str(ser.readline()).split("'")[1].split('\\')[0].split(',')
					if len(mydata)==23:
						if mydata[1]=='1':
							streamlineA = [int(x) for x in mydata]
						elif mydata[1]=='2':
							streamlineB = [int(x) for x in mydata]
						elif mydata[1]=='3':
							streamlineC = [int(x) for x in mydata]
				except Exception as e:
					print(e)
					print("FAILED")
			timestampA=(streamlineA[0]-start_time)/1000
			timestampB=(streamlineB[0]-start_time)/1000
			timestampC=(streamlineC[0]-start_time)/1000

			# print(streamline[16])
			accel_x.points_list_t[0].append((timestampB,streamlineB[14]/1000))
			accel_y.points_list_t[0].append((timestampB,streamlineB[15]/1000))
			# accel_x.points_list_t[0].append((timestampB,2))
			# accel_y.points_list_t[0].append((timestampB,2))

			brake_tps_steering.points_list_t[0].append((timestampA,(streamlineA[11]-streamlineA[10])/2)) ##### metatroph### check
			brake_tps_steering.points_list_t[1].append((timestampA,streamlineA[3]/2))
			# brake_tps_steering.points_list_t[2].append((timestampA,streamlineA[14]*2))# metatroph
			brake_tps_steering.points_list_t[2].append((timestampA,0))# metatroph

			gear_rpm_speed.points_list_t[0].append((timestampA,streamlineA[4]*20))#gear
			gear_rpm_speed.points_list_t[1].append((timestampA,(streamlineA[2]*68/60)/100))#rpm
			gear_rpm_speed.points_list_t[2].append((timestampA,streamlineA[13]))#GPSspeed

			roll_pitch.points_list_t[0].append((timestampA,0))
			roll_pitch.points_list_t[1].append((timestampA,0))
			roll_pitch.points_list_t[2].append((timestampA,0))

			shock_travel.points_list_t[3].append((timestampB,int(streamlineB[3])*(-0.2904)+219-RR_lin))
			shock_travel.points_list_t[2].append((timestampB,int(streamlineB[6])*(-0.2929)+217-RL_lin))
			shock_travel.points_list_t[1].append((timestampB,int(streamlineB[9])*0.3045+151-FR_lin))
			shock_travel.points_list_t[0].append((timestampB,int(streamlineB[12])*(-0.2575)+216-FL_lin))

			# accel_x.points_list_m[0].append((streamline[3],streamline[10]))
			# accel_y.points_list_m[0].append((streamline[3],streamline[11]))
			# brake_tps_steering.points_list_m[0].append((streamline[3],(streamline[41]-streamline[40])/2))
			# brake_tps_steering.points_list_m[1].append((streamline[3],streamline[16]))
			# brake_tps_steering.points_list_m[2].append((streamline[3],streamline[33]))

			# gear_rpm_speed.points_list_m[0].append((streamline[3],streamline[15]))
			# gear_rpm_speed.points_list_m[1].append((streamline[3],streamline[14]))
			# gear_rpm_speed.points_list_m[2].append((streamline[3],streamline[9]))

			# roll_pitch.points_list_m[0].append((streamline[3],streamline[23]))
			# roll_pitch.points_list_m[1].append((streamline[3],streamline[23]))
			# roll_pitch.points_list_m[2].append((streamline[3],streamline[23]))

			# shock_travel.points_list_m[0].append((streamline[3],streamline[23]))
			# shock_travel.points_list_m[1].append((streamline[3],streamline[23]))
			# shock_travel.points_list_m[2].append((streamline[3],streamline[23]))
			# shock_travel.points_list_m[3].append((streamline[3],streamline[23]))
			# brake_tps_steering.change = gear_rpm_speed.change = shock_travel.change = True= roll_pitch.change
			accel_x.change = accel_y.change = brake_tps_steering.change = gear_rpm_speed.change  = shock_travel.change=roll_pitch.change = True
			# self.i+=0.016
			# global j
			# j+=0.5
			# track_map.raw_coords=temp[int(j)%len(temp)]
			# ##create each sector
			# # sector1.currenttime = timesectors(streamline[5],1)
			# # #sector1.lap = int(self.i)
			# # sector2.currenttime = timesectors(streamline[5],2)
			# # #sector2.lap = int (self.i)
			# # sector3.currenttime = timesectors(streamline[5],3)
			# # #sector3.lap = int(self.i)
			rpm.progresslvl = (streamlineA[2]*68/600)  #(1+math.sin(4*math.pi*self.i))*5
			# # utclbl1.utctime = accel_x.points_list_t
			# # utclbl1.utcdate = accel_y.points_list_t
			slipratiosector.sectorvalue="0"
			gripsector.sectorvalue = str(streamlineB[15])
			understeersector.sectorvalue="0"
			gearlbl.currentgear = streamlineA[4]
			speedlbl.currentspeed = streamlineA[13]
			tpsgauge.tpsvalue = streamlineA[3]/2
			brakegauge.brakevalue =(streamlineA[19]+streamlineA[20]-180)/17
			testtemp.temps = [streamlineC[2],streamlineC[3],streamlineC[4],streamlineC[5],streamlineC[6],streamlineC[7],streamlineC[8],streamlineC[9],streamlineC[10],streamlineC[11],streamlineC[12],streamlineC[13],streamlineC[14],streamlineC[15],streamlineC[16],streamlineC[17]]
			gg_diagram.value = [streamlineB[15],streamlineB[14]]
			bbprogress.bbvalue = streamlineA[15]
			coolantsector.sectorvalue = str(streamlineA[5])
			# oilprsector.sectorvalue = str(streamline[20])
			batterysector.sectorvalue = str(round(streamlineA[7]*0.027,2))
			afrsector.sectorvalue = str(streamlineA[6]*0.0078125)
			# errorsector.sectorvalue = errorfunc(streamline[17])

		##### creates the error message #
		### errorslistc has the errors #
		##### argument error is 11 bits #
		### each one represents an error from the errorslist #
		##### errors may be more than one #
		### errors return through errormessage #
		def errorfunc(self,error):
			errorslist = [11]
			errormessage = [11]
			for i,x in enumerate(error):
				if self.error[i] == '1':
					errormessage.append(self.errorslist[i])
			return errormessage

		def roll_pitch(self,*args):
			pass

		##### sectors made like shit #
		####laptime splitting in sectors #
		##### sector must pass in the function as a str #
		####is called whenever getdata() is called :( #
		def timesectors(self,laptime,sector):
			if self.sector == '1':
				lapt1 = self.laptime
				return lapt1
			if self.sector == '2':
				lapt2 = self.laptime-lapt1
				return lapt2
			if self.sector == '3':
				lapt3 = self.laptime-(lapt2+lapt1)
				return lapt3


	try:
		TelemetryApp().run()
	except Exception as e:
		# ser.close()

		raise e
