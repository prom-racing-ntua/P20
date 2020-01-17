#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

#custom class imports

Builder.load_string('''
<Parametric_Label>:
    Label:
        text: str(root.name1)
        color: root.color1
        pos_hint: {"x":0, "y":0.5}
        size_hint: 0.5, 0.5
        font_size: root.font1
    Label:
        text: str(root.name2)
        color: root.color2
        pos_hint: {"x":0, "y":0}
        size_hint: 0.5, 0.5
        font_size: root.font2
    
''')


class Parametric_Label(FloatLayout):
    """A widget facilitating a parametric progressbar consisting of 20 seperate pieces \n
        Type:FloatLayout
        Uses Progress_Bar class 
    \n
    Parameters: \n
        name: StringProperty
        value: NumericProperty
        max_value: NumericProperty
        active_blocks: NumericProperty(how many out of 20 blocks will be lit)
        color: ColorProperty(list of 3 or 4 floats between (0.0-1.0) representing [red,green,blue,alpha])
        orientation: OptionProperty inherited from BoxLayout, defaults to ‘horizontal’. Can be ‘vertical’ or ‘horizontal\n 
    Update Functionality:
        Changing the value of value automatically updates the active_blocks and triggers an update of the actual progressbar.
    """
    name1 = StringProperty()
    name2 = StringProperty()
    color1 = ColorProperty([1,1,1,1])
    color2 = ColorProperty([1,1,1,1])
    font1 = StringProperty(defaultvalue="24sp")
    font2 = StringProperty(defaultvalue="16sp")

    def __init__(self, **kwargs):
        super(Parametric_Label, self).__init__(**kwargs)
