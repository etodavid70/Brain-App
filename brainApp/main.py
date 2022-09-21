
import kivy
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.image import Image

from kivy.animation import Animation, AnimationTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, TransitionBase, ScreenManager, FadeTransition, FallOutTransition,SlideTransition, CardTransition, ShaderTransition, SwapTransition, WipeTransition, RiseInTransition
from kivy.app import App, runTouchApp

from kivy.lang import Builder
from math import *
import random

from maine import iq_questions
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.config import Config

Config.set("graphics", 'resizable', 'true')


# Window.clearcolor=(1,1,1,1)
# Window.size=(450,650)


purple=(0.4, 0.1, 0.3, 1)
red=(0.4, 0.08, 0.08, 1)
blue=(0.008, 0.008, 1, 1)
green=(0.08, 0.08, 0.45, 1)
cyan=(0.08, 0.45, 0.45, 1)
brown=(0.3, 0.08, 0.08, 1)
non=(0,0,0,1)
grey=(1,1,1,1)

r= 0.5
g=0
b=0.5

btn_size_main=(0.3, 0.3)


#popup_math=Popup(tittle='game over', content=Label(text=f'Your score is {math_score}'), size_hint=(None, None), size=(400, 400), auto_dismiss=False)



main_box= BoxLayout(orientation="vertical")

up_title= Button(text="BrainApp", font_size=40,background_normal='orange_btn2.png',
            background_down='blue_btn2.png', size_hint=(1, 0.1), font_name='times.ttf')



back_to_menu_calc=Button(text = ' BACK', font_size= 30, size_hint=(1, 0.5), background_normal='orange_btn2.png',background_down='orange_btn2.png', font_name="slant.TTF",)
back_to_menu_setn=Button(text = ' BACK', font_size= 30, size_hint=(1, 0.5),background_normal='orange_btn2.png',background_down='orange_btn2.png', font_name="slant.TTF",)

back_to_main_iq=Button(text = 'BACK', font_size= 30, size_hint=(.2, 0.2),pos=(10,0), background_normal='orange_btn2.png',background_down='orange_btn2.png',font_name="slant.TTF",)

# first screen
first_page=Screen(name="start_page")

first=FloatLayout()





            
tutorial_btn=Button(
            text= "TUTORIALS",
            size_hint= btn_size_main,
            font_size=15,
            background_normal='orange_btn.png',
            background_down='orange_btn.png',
            font_name="slant.TTF",
            border=(30,30,30,30),
            pos_hint={'x': .1,'y': .5  },
            opacity=0
            )
            
menu_btn=Button(
            text="MENU",
            size_hint=btn_size_main,
            background_normal='purple_btn.png',
            background_down='purple_btn.png',
            font_name="slant.TTF",
            border=(30,30,30,30),
            pos_hint={'x': .1,'y': .2  },
            font_size=15,
            opacity=0)
            
mathbuilder_btn=Button(
            text= """MATH 
BUILDER""",
            size_hint= btn_size_main,
            background_normal='blue_btn.png',
            background_down='blue_btn.png',
            font_name="slant.TTF",
            border=(30,30,30,30),
            pos_hint={'x': .5,'y': .5  },
            font_size=15,
            opacity=0)
        
iq_builder_btn=Button(
            text="""   IQ 
BUILDER""",
            font_name="slant.TTF",
            size_hint= btn_size_main,
            background_normal='green_btn.png',
            background_down='green_btn.png',
            border=(30,30,30,30),
            pos_hint={'x': .5,'y': .2  },
            font_size=15,
            opacity=0
             )



first.add_widget(tutorial_btn)
first.add_widget(mathbuilder_btn)
first.add_widget(menu_btn)
first.add_widget(iq_builder_btn)
first_page.add_widget(main_box)
#first_page.add_widget(image)

main_box.add_widget(up_title)
main_box.add_widget(first)
#main_box.add_widget(down_title)

def animation1 (instance):
    anim = Animation(opacity=1, duration= 2.)
    anim += Animation(  duration=2.) #background_color=cyan,

    anim.start(tutorial_btn) 

def animation2 (instance):
    anim = Animation(opacity=1, duration= 2.)
    anim += Animation(   duration=2.) #background_color=purple,
    anim.start(menu_btn) 

def animation3 (instance):
    anim = Animation(opacity=1, duration= 2.)
    anim += Animation ( duration=2.) #background_color=purple,
    anim.start(mathbuilder_btn) 

def animation4 (instance):
    anim = Animation(opacity=1, duration= 2.)
    anim += Animation( duration=2.) #background_color=cyan
    anim.start(iq_builder_btn) 


Clock.schedule_once(animation1 )
Clock.schedule_interval(animation2, 3 )
Clock.schedule_interval(animation3, 5)
Clock.schedule_interval(animation4, 7 )



# Menu screen
b_box=Screen(name="menu")
c=RelativeLayout()
up_title2= Button(text="BrainApp", font_size=40,background_normal='orange_btn2.png',
            background_down='orange_btn2.png', font_name='times.ttf',size_hint=(1, 0.1),pos_hint={'x': 0,'y': .9  } )

settings_btn = Button(text = 'SETTINGS', size_hint=(0.66, 0.2),pos_hint={'x': .167,'y': .6  },font_name="slant.TTF",
background_normal='blue_btn2.png',
background_down='blue_btn2.png',
border=(30,30,30,30))

calculator_btn = Button(text = 'CALCULATOR', size_hint=(.66, 0.2), pos_hint={'x': .167,'y': .3  },font_name="slant.TTF",
background_normal='calc.jpg',
background_down='calc.jpg',
border=(30,30,30,30),)


back_btn= Button(text = ' BACK', font_size= 30, size_hint=(.66, 0.2), background_normal='orange_btn2.png',background_down='orange_btn2.png', pos_hint={'x': .167,'y': 0  }, font_name="slant.TTF",)


c.add_widget(up_title2)
c.add_widget(settings_btn)

c.add_widget(calculator_btn)
c.add_widget(back_btn)

b_box.add_widget(c)


# third screen


setting_screen=Screen(name="settings")


settings=BoxLayout(orientation="vertical")

settings_display= Button(text="Math Builder Timer (in minutes)",background_normal='purple_btn2.png',background_down='purple_btn2.png', font_name='slant.TTF')
settings.add_widget(settings_display)

slider_math=Slider(min= 0, max= 5, step= .5, value=1)
settings.add_widget(slider_math)

slider_math_display = Label(text ='1', color= red, font_size= 30,font_name='Lcd.ttf',)
settings.add_widget(slider_math_display)



difficulty_display= Button(text="Difficulty level (Maths)",background_normal='purple_btn2.png',background_down='purple_btn2.png', font_name='slant.TTF')
settings.add_widget(difficulty_display)

difficulty_slider=Slider(min= 1, max= 3, step= 1)
settings.add_widget(difficulty_slider)

difficulty_slider_display=Label(text ='1', color= red, font_size= 30,font_name='Lcd.ttf')
settings.add_widget(difficulty_slider_display)





settings_display2= Button(text="IQ Builder Timer (in minutes) ",background_normal='green_btn2.png',background_down='green_btn2.png',  font_name='slant.TTF')
settings.add_widget(settings_display2)

slider_iq=Slider(min= 0, max= 5, step= .5, value=1)
settings.add_widget(slider_iq)


slider_iq_display = Label(text ='1', color= red, font_size= 30,font_name='Lcd.ttf')
settings.add_widget(slider_iq_display)


#back2=Button(text = ' BACK', font_size= 30, size_hint=(1, 0.5), background_color=(b, r,g,0.8))
settings.add_widget(back_to_menu_setn)


setting_screen.add_widget(settings)









def on_value2 (self,instance):
        slider_iq_display.text = str(slider_iq.value)
        

def on_value1 (self, instance):
      slider_math_display.text = str(slider_math.value)

def on_value3 (self, instance):
      difficulty_slider_display.text = str(difficulty_slider.value)


slider_math.bind(value = on_value1)
slider_iq.bind(value = on_value2)
difficulty_slider.bind(value = on_value3)




#tutorial page (page layout)s

tutorial_screen = Screen(name="tutor")

layout=GridLayout(cols=1, spacing=10, size_hint_y=None)
layout.bind(minimum_height=layout.setter('height'))


back_to_main_tuto=Button(text = 'BACK', font_size= 30, height=40,size_hint_y=None, background_color=red)

for i in range(4):
    btn= Label(text=f'tutorials {i}', size_hint_y=None, height=40, color=brown)
    layout.add_widget(btn)
layout.add_widget(back_to_main_tuto)
   
root= ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)



layout2=GridLayout(cols=1, spacing=10, size_hint_y=None)
layout2.bind(minimum_height=layout2.setter('height'))

for x in range (4):
    about_btn= Label(text=f'tutorials {x}', size_hint_y=None, height=40, color=(g,r, b, 0.9))
    layout2.add_widget(about_btn)


root2= ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root2.add_widget(layout2)

tutor_page= PageLayout()

tutor_page.add_widget(root)
tutor_page.add_widget(root2)

tutorial_screen.add_widget(tutor_page)




#math screen
maths_screen=Screen(name="maths")

math=RelativeLayout()

score_maths=0
    
#image1=Image(source="bg1.jpg", size_hint=(1, 1), opacity=.2)

#start_againb=Button(text="START AGAIN", font_size=10, size_hint=(0.1, 0.1))
purple=(0.9999,0.,0.99999,1)

# popup_math=Popup(title='game over', content=Label(text=f'Your score is {score_maths}'), size_hint=(None, None), size=(400, 400), auto_dismiss=True)


operators =["/", "*", "+", "-"]
border=(5,5,5,5)

time_maths=slider_math.value

question_display=Button(text= """PRESS START 
TO START""",
background_normal='orange_btn2.png',
background_down='orange_btn2.png',
font_size=40, font_name='slant.TTF', 
size_hint= (1, .2), 

border=(30,30,30,30),
pos_hint={'x':0,'y': .8  }, )

user_answer= TextInput( text="", multiline=True, background_color="white",font_size=40,size_hint= (.4, .1), pos_hint={'x':0.2,'y': .55  },
 font_name="slant.TTF", )

solution_math=Label(text="", size_hint= (.33,0.2), pos_hint={'x':0,'y': 0.2  } , color=red,font_name='slant.TTF' )
status_math=Label(text="", size_hint= (.33,0.2), pos_hint={'x':.33,'y': .2  }, color=red,font_name='slant.TTF' )
timer_maths=Label(text="", font_size=80 , size_hint= (.33,0.2), pos_hint={'x':.67,'y': .2 }, color=red, font_name='Lcd.ttf')


submit=Button(text="SUBMIT",font_name="slant.TTF", disabled= True,
size_hint= (.2, .18), 
background_normal='orange2.png',
background_down='orange2.png',
border=(30,30,30,30),
pos_hint={'x':.6,'y': .4  },  )

end_maths=Button(text="END", font_name="slant.TTF",  
size_hint= (.2,0.2), 
background_normal='orange_btn2.png',
background_down='orange_btn2.png',
border=(30,30,30,30),
pos_hint={'x':.4,'y': 0  },  )


start=Button(text="START", font_name="slant.TTF",
size_hint= (.2, .18), 
background_normal='orange2.png',
background_down='orange2.png',
border=(30,30,30,30),
pos_hint={'x':.6,'y': .6  },)



math.add_widget(question_display)
math.add_widget(user_answer) 
math.add_widget(submit)
math.add_widget(start)




math.add_widget(solution_math)
math.add_widget(timer_maths)
math.add_widget(status_math)

math.add_widget(end_maths)

    



    




def start_math(instance):
    global score_maths
    global difficulty_slider
    n=10**difficulty_slider.value
    anim = Animation( opacity=1, duration=1.5)
    anim2 = Animation( opacity= 0.08, duration= 1.5)
    anim.start(question_display)
    anim.start(submit)
    anim2.start(start)
    #anim2.start(start) 
    start.disabled=True 
    submit.disabled=False
    
    



    number1=str(random.randint(2, 1000))
    operations=random.choice(operators)
    number2=str(random.randint(2, n))   
    quest=number1+"  "+operations+"  "+number2
    question_display.text= quest
    status_math.text="" 
    solution_math.text=""



def submit_ans(instance):
    global status
    global user_answer
    global score_maths
    global solution_math
    global status_math
    global popup_math


    anim = Animation(opacity=0.08, duration= 1.5)
    anim2= Animation(opacity=1, duration=1.5)
    anim.start(question_display)
    #anim.start(submit)
    anim2.start(start)
    submit.disabled=True
    start.disabled=False


    #popup_math.open()

    text= question_display.text
    if text:
        solution2 = str(round(eval(question_display.text)))
        
        


    if user_answer.text==solution2:
        user_answer.text=""
        score_maths+=1
        status_math.text= f"""CORRECT!
your score is 
 {score_maths}""" 
        solution_math.text=f'''correct answer: 
''' +str(solution2)
    else:
        status_math.text=f"""WRONG!
your score is 
{score_maths}"""
        user_answer.text=""
        solution_math.text=f'''correct answer: 
''' +str(solution2)



        

# popup_math=Popup(title='game over', content=Label(text=f'Your score is {score_maths}'), 
# size_hint=(None, None), size=(400, 400), auto_dismiss=True)


        
def game_over_maths (instance):
    global popup_math
    global score_maths
    global timer_maths
    global time_maths
    global status_math
    global solution_math
    global event2
    time_maths=0
    timer_maths.opacity=0
    status_math.text="" 
    solution_math.text=""

    popup_math=Popup(title='game over', content=Label(text=f'Your score is {score_maths}'), 
size_hint=(None, None), size=(200, 300), auto_dismiss=True)
    popup_math.bind(on_dismiss=go_back_to_main)

    popup_math.open()
    Clock.unschedule(event_math)
    


def math_clock():
    global time_maths
    global timer_maths
    global event_math
    time_maths=time_maths-1
    timer_maths.text=str(time_maths)
    
    
    if time_maths==0:
        game_over_maths(None)
    event_math=Clock.schedule_once(lambda dt: math_clock(), 1)


    

start.bind(on_press=start_math)
submit.bind(on_press=submit_ans)
end_maths.bind(on_press=game_over_maths)


maths_screen.add_widget(math)



    

#IQ SCREEN

iq_screen=Screen(name="iq")

iq=RelativeLayout()
#image1=Image(source="bg1.jpg", size_hint=(1, 1), opacity=.2)
score_iq=0


purple=(0.4, 0.1, 0.3, 1)
red=(0.4, 0.08, 0.08, 1)
blue=(0.08, 0.4, 0.08, 1)
green=(0.08, 0.08, 0.45, 1)
cyan=(0.08, 0.45, 0.45, 1)
brown=(0.3, 0.08, 0.08, 1)




question_display_iq=Button(text= "PRESS START TO START",font_size=20, font_name="slant.TTF",
size_hint= (1, .2), 
background_normal='orange_btn2.png',background_down='orange_btn2.png',
border=(30,30,30,30),
pos_hint={'x':0,'y': .8  }, )

user_answer_iq= TextInput( multiline=False, background_color="white", 
foreground_color= red,font_size=40,size_hint= (.4, .1), pos_hint={'x':0.2,'y': .55  }, font_name="slant.TTF" )

true_answer_iq=""
time_iq=slider_iq.value

answer_iq_display=Label(text="",  font_size=15, size_hint= (.5,0.2), pos_hint={'x':.0,'y': 0.2  } , color=red, font_name='PatrickHand-Regular.ttf' ) 
timer_iq=Label(text="", font_size=60 , size_hint= (.1,0.2), pos_hint={'x':.8,'y': .2 }, color=red, font_name='Lcd.ttf')
status_iq=Label(text="", font_size=20, size_hint= (.2,0.2), pos_hint={'x':.6,'y': .2  }, color=red, font_name='PatrickHand-Regular.ttf' )

submit_iq=Button(text="SUBMIT",font_name="slant.TTF", disabled= True, font_size=15,
size_hint= (.2, .18), 
background_normal='orange2.png',
background_down='orange2.png',
border=(30,30,30,30),
pos_hint={'x':.6,'y': .4  },  )

start_iq=Button(text="START", font_name="slant.TTF",font_size=15,
size_hint= (.2, .18), 
background_normal='orange2.png',
background_down='orange2.png',
border=(30,30,30,30),
pos_hint={'x':.6,'y': .6  },)

end_iq=Button(text="END", font_name="slant.TTF", font_size=15,

size_hint= (.2,0.2), 
background_normal='orange_btn2.png',
background_down='orange_btn2.png',
border=(30,30,30,30),
pos_hint={'x':.4,'y': 0  },  )


iq.add_widget(question_display_iq)



iq.add_widget(user_answer_iq)
iq.add_widget(submit_iq)
iq.add_widget(start_iq)



iq.add_widget(answer_iq_display)
iq.add_widget(timer_iq)
iq.add_widget(status_iq)







#btns2.add_widget(back_to_main_iq)
iq.add_widget(end_iq)



question_number=0

xout=random.choice(iq_questions)

def alternate():
    global xout
    xout=random.choice(iq_questions)





def game_over_iq (instance):
    global popup_iq
    global timer_iq
    global time_iq
    global status_iq
    global answer_iq_display
    time_iq=0
    timer_iq.opacity=0
    
    status_iq.text=""
    answer_iq_display.text=""

    popup_iq=Popup(title='game over', content=Label(text=f'Your score is {score_iq}!'), 
    size_hint=(None, None), size=(200, 300), auto_dismiss=True)
    popup_iq.open()
    popup_iq.bind(on_dismiss=go_back_to_main)
    event_iq.cancel()


def iq_clock():
    global time_iq
    global timer_iq
    global event_iq

    time_iq=time_iq-1
    timer_iq.text=str(time_iq)


    if time_iq==0:
        game_over_iq(None)
    event_iq=Clock.schedule_once(lambda dt: iq_clock(), 1)
        

def start_iq_function(instance):
    
    alternate()
    n=random.randint(0, 10)
    global score
    global iq_questions
    global question_display_iq
    global true_answer_iq
    global question_number

    question_number+=1
    
    anim = Animation( opacity=1, duration=2.)
    anim.start(question_display_iq)
    anim.start(submit_iq)

    anim2= Animation(opacity=0.2, duration= 3.)
    anim2.start(start_iq)
    start_iq.disabled=True
    submit_iq.disabled= False


    

    question_display_iq.text=f'Question {question_number}: {xout[0]}'

    true_answer_iq=xout[1]
    status_iq.text=""
    answer_iq_display.text=""



def submit_iq_function(instance):
    global xout
    global status_iq
    global user_answer_iq
    global score_iq
    global solution_iq
    global status_iq
    global true_answer_iq

    anim = Animation( opacity=0.2, duration=2.)
    anim.start(question_display_iq)
    anim.start(submit_iq)
    
    anim2= Animation(opacity=1, duration= 3.)
    anim2.start(start_iq)
    start_iq.disabled=False
    submit_iq.disabled=True

    answer_iq_display.text=f'''Answer: {xout[1]}
Explanation:
{xout[2]}'''
   

    if user_answer_iq.text.upper()==true_answer_iq:
         
        user_answer_iq.text=""
        score_iq+=1
        status_iq.text=f"""CORRECT! 
your score: 
{score_iq}"""
        
    else:
        status_iq.text=f"""WRONG! 
your score: 
{score_iq}"""
        user_answer_iq.text=""




start_iq.bind(on_press=start_iq_function)
submit_iq.bind(on_press=submit_iq_function)
end_iq.bind(on_press=game_over_iq)

iq_screen.add_widget(iq)




#calculator

calculator_screen= Screen(name="calc")

operators =["/", "*", "+", "-"]
last_was_operator =None
last_Button= None


main_layout= BoxLayout(orientation= "vertical")
solution =TextInput(background_color="white", foreground_color=red,
multiline=True, halign= "right", font_size=35)

main_layout.add_widget(solution)
Buttons= [
[ "7", "8", "9", "/", ],
[ "4", "5", "6", "*", ],
[ "1", "2", "3", "+", ],
[ ".", "0", "C", "-", ],
["cos(", "factorial(", "exp("],
["sin(", "1/", "sqrt("],
["tan(", "(", "pow("],
["log(", ")", ","]
]




equal_Button=Button(background_normal='orange_btn2.png',background_down='orange_btn2.png',
text="=", font_size=30, background_color=brown,
pos_hint={"center_x": 0.5, "center_y": 0.5},
)






def on_Button_press(instance):
    global last_was_operator
    global last_Button
    current=solution.text
    Button_text= instance.text

    if Button_text =="C":
        solution.text=""
    else:
        if current and (
        last_was_operator and Button_text in operators):
            return
        elif current=="" and Button_text in operators:
            return
        else:
            new_text=current + Button_text
            solution.text = new_text
            last_Button=Button_text
            last_was_operator=last_Button in operators
            
for row in Buttons:
    h_layout= BoxLayout()
    for label in row:
        button= Button(background_normal='orange_btn.png',background_down='orange_btn.png',
        text=label, font_size=20, 
        pos_hint={"center_x": 0.5, "center_y": 0.5},)

        button.bind(on_press=on_Button_press)
        h_layout.add_widget(button)
    main_layout.add_widget(h_layout)


def on_solution(instance):
    global solution
    try:
        text= solution.text
        if text:
            solution2 = str(eval(solution.text))
            solution.text=solution2
    except: 
        solution=ZeroDivisionError
        solution.text="math error!"

main_layout.add_widget(equal_Button)
main_layout.add_widget(back_to_menu_calc)
equal_Button.bind(on_press=on_solution)

calculator_screen.add_widget(main_layout)








#main screen manager
trans= [ FadeTransition(duration=2.0),
 
  WipeTransition(duration=2.0)]


sm=ScreenManager(transition=random.choice(trans))

       

sm.add_widget(first_page)
sm.add_widget(b_box)
sm.add_widget(setting_screen)
sm.add_widget(tutorial_screen)
sm.add_widget(maths_screen)
sm.add_widget(iq_screen)
sm.add_widget(calculator_screen)


sm.current="start_page"


def switch_to_menu(instance):
    
   sm.current="menu"

def switch_to_settings(instance):
    
   sm.current="settings"


def go_back_to_main (instance):
   sm.current="start_page"
   

def switch_to_tutorial(instance):
   sm.current='tutor'

def switch_to_maths(instance):
   sm.current='maths'
   global time_maths
   global score_maths
   time_maths=60*slider_math.value
   timer_maths.opacity=1
   math_clock()
   #Clock.schedule_interval(lambda dt: math_clock(), 1)
   score_maths=0
   
   
   #start the math countdown
   
   




def switch_to_iq(instance):
   sm.current='iq'
   global time_iq
   global score_iq
   time_iq=60*slider_iq.value
   timer_iq.opacity=1
   iq_clock()
   #Clock.schedule_interval(iq_clock, 1)
   score_iq=0
   
   





def switch_to_calc(instance):
   sm.current="calc"



#popup_math.bind(on_dismiss=go_back_to_main)
#popup_iq.bind(on_dismiss=go_back_to_main)

tutorial_btn.bind(on_press=switch_to_tutorial)
menu_btn.bind(on_press=switch_to_menu)
settings_btn.bind(on_press=switch_to_settings)
#about_btn.bind(on_press=switch_to_about)
#back2.bind(on_self=switch_to_menu2)
back_btn.bind(on_press=go_back_to_main)
mathbuilder_btn.bind(on_press=switch_to_maths)
iq_builder_btn.bind(on_press=switch_to_iq)
calculator_btn.bind(on_press=switch_to_calc)
back_to_menu_setn.bind(on_press=switch_to_menu)
back_to_menu_calc.bind(on_press=switch_to_menu)
back_to_main_tuto.bind(on_press=go_back_to_main)
#back_to_main_math.bind(on_press=go_back_to_main)
back_to_main_iq.bind(on_press=go_back_to_main)




class BrainApp(App):
    def build(self):
        return sm



app=BrainApp()
app.run()       

