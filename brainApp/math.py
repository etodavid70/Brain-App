import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

class MainApp(App):
    def build(self):
        self.operators =["/", "*", "+", "-"]
        self.last_was_operator =None
        self.last_button= None


        main_layout= BoxLayout(orientation= "vertical")

        self.random_text =Label(text="Press Start Button to Start", font_size=35)

        self.solution=Label(text="", font_size=35)

        self.user_input =TextInput(background_color="black", foreground_color='blue',
        multiline=True, halign= "right", font_size=35)

        self.status=Label(text="")

        
        main_layout.add_widget(self.random_text)
        main_layout.add_widget(self.solution)
        main_layout.add_widget(self.user_input)
        main_layout.add_widget(self.status)
        
        

        buttons= [
           [ "7", "8", "9" ],
           [ "4", "5", "6" ],
           [ "1", "2", "3" ],
           [ ".", "0", "C" ],
           
            ]

        for row in buttons:
            h_layout= BoxLayout()
            for label in row:
                button= Button(
                    text=label, font_size=30, background_color="black",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        start_button=Button(
            text="Start/Continue", font_size=20, background_color="#006400",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        submit_button=Button(
            text="Submit", font_size=20, background_color="#006400",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        start_button.bind(on_press=self.generate_number)
        main_layout.add_widget(start_button)

        submit_button.bind(on_press=self.submit_ans)
        main_layout.add_widget(submit_button)


        return main_layout

    def on_button_press(self, instance):
        current=self.user_input.text
        button_text= instance.text

        if button_text =="C":
            self.user_input.text=""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current=="" and button_text in self.operators:
                return
            else:
                new_text=current + button_text
                self.user_input.text = new_text
        self.last_button=button_text
        self.last_was_operator=self.last_button in self.operators
    
    
   

    def generate_number(self, instance):
        number1=str(random.randint(0, 1000))
        operations=random.choice(self.operators)
        number2=str(random.randint(0, 20))   
        question_display=number1+operations+number2
        self.random_text.text= question_display
        self.status.text="" 
        self.solution.text=""
    
    def submit_ans(self, instance):
            text= self.random_text.text
            if text:
                solution2 = str(eval(self.random_text.text))
                self.solution.text=solution2
        
        
                if self.user_input.text==solution2:
                    self.status.text="CORRECT!"  
                    self.user_input.text=""
                else:
                    self.status.text="WRONG!"
                    self.user_input.text=""
    


if __name__=="__main__":
    app=MainApp()
    app.run()


