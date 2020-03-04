#library imports
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

#custom class imports
from pc_status import Pc_Status

Builder.load_string('''
ScrollView:
    do_scroll_x: False
    do_scroll_y: True
    
    Label:
        size_hint: (1, None)
        #size: Window.size
        text: "i don't know what the fuck i'm doing rn/n" * 100
''')

class Diagnostics(Screen):
    data = ListProperty()
    layout = GridLayout(cols=1, spacing=10, size_hint_y=None)

    def __init__(self, **kwargs):
        super(Diagnostics, self).__init__(**kwargs)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        
        root.add_widget(self.layout)        
        self.add_widget(root)
    