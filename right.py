#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from time_table import Time_Table



class Right(FloatLayout):
    def __init__(self, **kwargs):
        super(Right, self).__init__(**kwargs)
        self.table = Time_Table(pos_hint = {'x':0,'y':0.5}, size_hint = (1,0.5)  )
        self.add_widget(self.table)
