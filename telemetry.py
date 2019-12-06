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

#custom class imports
from left import Left
from middle import Middle
from right import Right

class MainScreen(App):

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.fullscreen = False
        mainscreen = GridLayout()
        mainscreen.cols = 3
        left = Left()
        middle = Middle()
        right = Right()

        mainscreen.add_widget(left)
        mainscreen.add_widget(middle)
        mainscreen.add_widget(right)
        return mainscreen


if __name__ == '__main__':
    try:
        MainScreen().run()
    except Exception as e:
        raise e        
