#library imports
import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

#custom class imports
from color_block import Color_Block

Builder.load_string('''
<Progress_Bar>:
    canvas.before:
        Color:
            rgba: 1,1,1,0.5
        Line:
            rectangle: self.x, self.y, self.width, self.height
''')

class  Progress_Bar(BoxLayout):
    """A widget representing a progressbar consisting of 20 seperate pieces \n
        Type:BoxLayout
        Uses Color_Block class
    \n
    Parameters: \n
        active_blocks: NumericProperty(how many out of 20 blocks will be lit)
        color: ColorProperty(list of 3 or 4 floats between (0.0-1.0) representing [red,green,blue,alpha])
        orientation: OptionProperty inherited from BoxLayout, defaults to ‘horizontal’. Can be ‘vertical’ or ‘horizontal\n 
    Update Functionality:
        Changing the value of active blocks automatically updates the active color blocks
    """
    active_blocks = NumericProperty()
    color = ColorProperty()

    def __init__(self, **kwargs):
        super(Progress_Bar, self).__init__(**kwargs)

        #widgets go in reverse
        self.add_widget(Color_Block(color=[1,0,0,1]))
        for i in range(18, -1, -1):
            self.add_widget(Color_Block(color=self.color))
        self.bind(active_blocks=self.update_active)

    def update_active(self, obj, value):
        s = value
        for i in self.children:
            a = 1 if s>0 else 0
            i.opacity = a
            s -= 1
        

