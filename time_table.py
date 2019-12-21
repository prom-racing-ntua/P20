from kivy.app import App
from kivy.lang import Builder
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from time_label import Time_Label



Builder.load_string("""
<Time_Table>:


""")
class Time_Table(GridLayout):
    def __init__(self,**kwargs):
        super(Time_Table,self).__init__(**kwargs)
        self.cols = 5
        self.add_widget(Label(text=""))
        self.add_widget(Label(text="Lap"))
        self.add_widget(Label(text="Sector1"))
        self.add_widget(Label(text="Sector2"))
        self.add_widget(Label(text="Sector3"))
        self.add_widget(Label(text="this"))
        for i in range(4):
            self.add_widget(Time_Label(colortime="30.5", colortext=[1,0,0,1]))
        self.add_widget(Label(text="last"))
        for i in range(4):
            self.add_widget(Time_Label(colortime="30.5", colortext=[1,0,0,1]))
        self.add_widget(Label(text="best"))
        for i in range(4):
            self.add_widget(Time_Label(colortime="30.5", colortext=[1,0,0,1]))
        print(self.ids)
