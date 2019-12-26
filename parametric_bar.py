#library imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

#custom class imports
from progress_bar import Progress_Bar

Builder.load_string('''
<Parametric_Bar>:
    Label:
        text: str(root.value)
        color: root.color
        pos_hint: {"x":0.6, "y":0.1}
        size_hint: 0.4, 0.9
        font_size: "24sp"
''')

class Parametric_Bar(FloatLayout):
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
    name = StringProperty()
    value = NumericProperty()
    max_value = NumericProperty()
    orientation = StringProperty()
    color = ColorProperty()
    active_blocks = NumericProperty()

    def __init__(self, **kwargs):
        super(Parametric_Bar, self).__init__(**kwargs)

        #calculating active sectors (x/20)
        self.active_blocks = (self.value*20)/self.max_value

        #setting up widgets
        self.label = Label(text=self.name, pos_hint={"x":0, "y":0}, size_hint=(1, 0.1))
        self.progress = Progress_Bar(pos_hint={"x":0, "y":0.15}, size_hint=(0.5, 0.9), orientation = self.orientation, color=self.color, active_blocks=self.active_blocks)
        
        #adding widgets
        self.add_widget(self.label)
        self.add_widget(self.progress)

        #for testing
        Clock.schedule_interval(self.rng, 0.5)

        self.bind(value=self.update)

    #for testing, random
    def rng(self, dt):
        self.value = random.randint(0,self.max_value)
    
    def update(self, obj, value):
        self.active_blocks = (self.value*20)/self.max_value
        self.progress.active_blocks = self.active_blocks


