import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

class MainApp(App):
    def build(self):


        main_layout= BoxLayout(orientation= "vertical")

        self.random_text =Label(text="Press Start Button to Start", font_size=35)

        self.solution=Label(text="", font_size=35)

        
        self.status=Label(text="")

        
        main_layout.add_widget(self.random_text)
        
        main_layout.add_widget(self.status)
        
        

        

        start_button=Button(
            text="Start/Continue", font_size=20, background_color="#006400",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        submit_button=Button(
            text="Submit", font_size=20, background_color="#006400",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        start_button.bind(on_press=self.start)
        main_layout.add_widget(start_button)

        submit_button.bind(on_press=self.submit_ans)
        main_layout.add_widget(submit_button)


        return main_layout

    def on_button_press(self, instance):
        pass
    
   

    def start(self, instance):
        pass
    
    def submit_ans(self, instance):
        pass
        
        
               
if __name__=="__main__":
    app=MainApp()
    app.run()


