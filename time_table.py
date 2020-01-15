from kivy.app import App
from kivy.lang import Builder
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from time_label import Time_Label

labels = ["", "Lap", "Sector1", "Sector2", "Sector3", "this", "last", "best"]

colors = {
    'green': [],
    'purple': [],
    'red': []
}

Builder.load_string("""
<Time_Table>:


""")
class Time_Table(GridLayout):
    def __init__(self,**kwargs):
        super(Time_Table,self).__init__(**kwargs)
        self.cols = 5
        for i in range(5):
            self.add_widget(Label(text = labels[i]))
        for i in range(3):
            self.add_widget(Label(text=labels[i+5]))
            clr = [128/255., 0, 128/255., 1] if i == 2 else [1, 0, 0, 1]
            for j in range(4):
                self.add_widget(Time_Label(colortime="30.5", colortext=clr))

        #for x in self.children:    
            #print(x)
