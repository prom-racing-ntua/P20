from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem

class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # use a (r, g, b, a) tuple
        blue = (0, 0, 1.5, 2.5)
        red = (2.5, 0, 0, 1.5)


        tab=TabbedPanel()
        tabitem=TabbedPanelItem()
        tab.add_widget(tabitem)
        layout.add_widget(tab)

        btn =  Button(text='Touch me!', background_color=blue, font_size=120)
        btn.bind(on_press=self.callback)
        btn2 =  Button(text='btn2', background_color=red, font_size=120)
        tabitem.add_widget(btn)
        tabitem.add_widget(btn2)

        self.label = Label(text="------------", font_size='50sp')
        tabitem.add_widget(self.label)

        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        tabitem.add_widget(btn1)
        self.lbl1 = Label(text="test")
        tabitem.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        tabitem.add_widget(self.txt1)

        return layout

    def callback(self, event):
        print("button touched")  # test
        self.label.text = "button touched"

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "You wrote " + self.txt1.text

# run app
if __name__ == "__main__":
    MyApp().run()
