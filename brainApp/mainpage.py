import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation, AnimationTransition
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

class MainApp(App):
    def build(self):

        main_layout= BoxLayout(orientation= "vertical")

        
        dropdown = DropDown()

        btn1 = Button(text = 'settings', size_hint_y =None, height =40, background_color="yellow")
        btn1.bind(on_release= lambda btn: dropdown.select(btn1.text))
        dropdown.add_widget(btn1)

        btn2 = Button(text = 'tutorials', size_hint_y =None, height =40, background_color="yellow")
        btn2.bind(on_release= lambda btn: dropdown.select(btn2.text))
        dropdown.add_widget(btn2)


        btn3 = Button(text = 'high score', size_hint_y =None, height =40, background_color="yellow")
        btn3.bind(on_release= lambda btn: dropdown.select(btn3.text))
        dropdown.add_widget(btn3)


        btn4= Button(text = 'calculator', size_hint_y =None, height =40, background_color="yellow")
        btn4.bind(on_release= lambda btn: dropdown.select(btn4.text))
        dropdown.add_widget(btn4)


        btn5 = Button(text = 'about', size_hint_y =None, height =40, background_color="yellow")
        btn5.bind(on_release= lambda btn: dropdown.select(btn5.text))
        dropdown.add_widget(btn5)



        mainbutton=Button(text= 'MENU', size_hint= (None, None), pos= (0, 500), background_color="yellow")

        mainbutton.bind(on_release = dropdown.open)

        
        main_layout.add_widget(mainbutton)

        iq_builder=Button(text="IQ BUILDER", font_size=20, background_color="yellow")

        iq_builder.bind(on_press=self.display_iq_builder)

        main_layout.add_widget(iq_builder)

        anim = Animation(x=0, y=250, duration=4.)
        #anim = Animation(x=0, y=300, size=(80, 80), t='in_quad')
        anim.start(iq_builder)


        math_builder=Button(text="MATH BUILDER", font_size=20, background_color="yellow")

        math_builder.bind(on_press=self.display_math_builder)

        main_layout.add_widget(math_builder)

        return main_layout

    def display_iq_builder(self, instance):
        pass
    
    def display_math_builder(self, instance):
        pass
    

        
        

        #runTouchApp(mainbutton)

if __name__=="__main__":
    app=MainApp()
    app.run()


