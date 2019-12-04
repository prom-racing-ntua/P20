import kivy
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.widget import Widget
from kivy.uix.image import Image
#from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
from kivy.animation import Animation


class Image(FloatLayout):
    pass


#class Widgets(Widget):
 #   pass


#class Image(Image):
   # pass


class MyApp(App):
    def build(self):
        return FloatLayout()
    #def animate(self,instance)
        #return Image()
    #def build(self):
     #   return Image (source = 'icon.png')


#class PongApp(App):
   # def build(self):
      #  return PongGame()


if __name__ == '__main__':
    MyApp().run()
