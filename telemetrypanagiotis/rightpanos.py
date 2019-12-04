from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from customGraph import Graph
from kivy.garden.graph import LinePlot, MeshLinePlot
from promGraph import PromGraph
from sectors import *
from rpmbar import RPMbar
from gearlbl import GearLabel
from speedlbl import SpeedLabel
from warning_Label import WarningLabel
from tpsbar import TPSGauge
from brakegauge import BrakeGauge
from brakebiaspb import BrakeBiasPB
from tempsectors import TempSectors
from accel import Accel




class telemetry(Widget):
    right_column = FloatLayout()
    laps = Sectors(
    sectorname = "Lap",
    pos_hint = {'x':0,'y':0},
    size_hint = (0.03,0.13)
    )
    right_column.add_widget(laps)


class telemetrypanos(App):
    def build(self):
            return telemetry()

if __name__ == '__main__':
    telemetrypanos().run()
