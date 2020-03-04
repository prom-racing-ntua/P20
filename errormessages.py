#library imports
import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Builder.load_string('''
ScrollView:
    do_scroll_x: False
    do_scroll_y: True
    
    Label:
        size_hint: (1, None)
        #size: Window.size
        text: "i don't know what the fuck i'm doing rn/n" * 100
''')


class ErrorMessages(ScrollView):

    layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    
    def __init__(self, **kwargs):
        super(ErrorMessages, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        for i in range(100):
            self.box.add_widget(Label(text='errors{}'.format(i), size_hint=(1, None)))
        self.add_widget(self.box)
