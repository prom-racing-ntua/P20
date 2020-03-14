#library imports
from kivy.lang import Builder
from kivy.properties import ListProperty, BooleanProperty, StringProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from configparser import ConfigParser
from kivy.uix.recycleview import RecycleView


Builder.load_string('''
<RV>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width:1.25
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class RV(RecycleView):
    new_error = StringProperty()
    #index = 
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{}]
        self.bind(new_error=self.update)
        

    def update(self, obj, val):
        print(val)
        self.data.append({'text':str(val)})

