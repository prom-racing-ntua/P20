import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from kivy.app import App
import matplotlib.pyplot as plt

import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.boxlayout import BoxLayout

class Mygrid(BoxLayout):
    pass

class GridLayoutApp(App):
        def build(self):
            return Mygrid()


if __name__ == '__main__':
    GridLayoutApp().run()
