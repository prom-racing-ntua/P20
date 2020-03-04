#library imports
import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<ErrorMessages>:
    do_scroll_x: False
    do_scroll_y: True
''')


class ErrorMessages(ScrollView):

    def __init__(self, **kwargs):
        super(ErrorMessages, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        for i in range(100):
            self.box.add_widget(Label(text='errors{}'.format(i), size_hint=(1, None)))
        self.add_widget(self.box)
