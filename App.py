from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class MyWidgetContainer(BoxLayout):
    def __init__(self, **kwargs):


        super(MyWidgetContainer, self).__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        with self.canvas.before:
            Color(0.0, 0.4, 0.2, 2)  # Set the background color (R, G, B, A)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_rect, pos=self.update_rect)

        self.label = Label(text="fill in the form",
                           size_hint_y=None, height=50, font_size='20sp')
        
        self.text_input1 = TextInput(hint_text="Enter your name of the child",
                                    size_hint_y=None, height=50, font_size='20sp')
        
        self.text_input2 = TextInput(hint_text="Weekly Assessment",
                                    size_hint_y=None, height=50, font_size='20sp')
        
        self.text_input3 = TextInput(hint_text="Monthly Assessment",
                                    size_hint_y=None, height=50, font_size='20sp')
        
        self.text_input4 = TextInput(hint_text="Midterm",
                                    size_hint_y=None, height=50, font_size='20sp')
        
        self.text_input5 = TextInput(hint_text="End of Term" ,
                                     size_hint_y=None, height=50, font_size='20sp')
        

        self.button = Button(text="Click me!",
                             size_hint_y=None,size_hint_x=None, width=300,height=50, font_size='20sp')
        self.button.bind(on_press=self.display_message)
        
        self.add_widget(self.label)
        self.add_widget(self.text_input1)
        self.add_widget(self.text_input2)
        self.add_widget(self.text_input3)
        self.add_widget(self.text_input4)
        self.add_widget(self.text_input5)
        self.add_widget(self.button)
        
    def display_message(self, instance):
        name = self.text_input.text
        self.label.text = f"Hello, World! {name}"

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class HelloWorldApp(App):
    def build(self):
        return MyWidgetContainer()

if __name__ == "__main__":
    HelloWorldApp().run()
