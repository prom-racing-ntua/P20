import kivy
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, ColorProperty, StringProperty, BoundedNumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock




Builder.load_string('''
<Accel>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "assets/scope2.png"
        Color:
            rgba: 1,1,1,0.5
        Line:
            rectangle: self.x, self.y, self.width, self.height
    #Image:
        #pos_hint: {"center_x":0.5, "center_y":0.5}
        #source: "assets/red_dot.png"
        #size_hint: 0.05, 0.05        
        #opacity: 1
''')


class Accel(FloatLayout):
    #x = BoundedNumericProperty(50, min=0, max=100, errorvalue=50)
    #y = BoundedNumericProperty(50, min=0, max=100, errorvalue=50)

    acc = ListProperty()
    x = NumericProperty(defaultvalue=50)
    y = NumericProperty(defaultvalue=50)
    previous = ObjectProperty()

    def __init__(self, **kwargs):
        super(Accel, self).__init__(**kwargs)

        #self.bind(x=self.update)
        #self.bind(y=self.update)
        self.bind(acc=self.update)

    #implement a check for out of bounds
    def update(self, obj, value):
        anim = Animation(opacity=0)
        if self.previous is not None:
            self.previous.opacity = 0.7
            anim.start(self.previous)
            anim.bind(on_complete=self.remove)

        print(len(self.children))
        im = Image(pos_hint={"center_x": self.acc[0]/100, "center_y": self.acc[1]/100}, source="assets/red_dot.png", size_hint= (0.05, 0.05), opacity=1)
        self.add_widget(im)
        self.previous = im

    def remove(self, animation, widget):
        self.remove_widget(widget)
        

        
