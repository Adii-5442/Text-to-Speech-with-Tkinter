from cProfile import label
from tkinter import *
from turtle import color
from gtts import gTTS
from playsound import playsound
import os
import vlc

print('''Instructions:
        1.Type in the Dialogue Box whatever you want to convert.
        2.Always Save the file before playing to avoid Unexpected errors
                                                     ---By Darkfire''')
print(" ")
print("\U0001f600 \U0001f600 \U0001f600 ENJOY ! \U0001f600 \U0001f600 \U0001f600")
root = Tk()
root.geometry("350x310")
root.configure(bg='black')
root.title("SPEECH")


Label(root, text = "*SPEECH*", font = "system 20 bold", bg='black',foreground='white').pack()
Label(text ="By DarkFire", font = 'system 15 bold', bg ='black' , width = '20',foreground='white').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'system 15 bold', bg ='black',foreground='white',width=25).place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='60')
entry_field.place(x=20,y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('test.mp3')

def play():
    try:
        p = vlc.MediaPlayer("test.mp3")
        p.play()
    except:
        print("PLease Save a text first")

def exit():
    root.destroy()

def reset():
    Msg.set("")
Label(root,text="First save the file after entering",fg='white',bg='black').pack(side='bottom')

Button(root, text='SAVE',font='system 15 bold' , command=Text_to_speech,width='4',foreground='white',bg='green').place(x=20,y=140)

Button(root, text = "PLAY", font = 'system 15 bold' , command = play ,width = '4',foreground='white',bg='blue').place(x=100,y=140)

Button(root, font = 'system 15 bold',text = 'EXIT', width = '4' , command = exit, bg = 'Red',foreground='white').place(x=170 , y = 140)

Button(root, font = 'system 15 bold',text = 'RESET', width = '6' , command = reset,foreground='black',bg='yellow').place(x=240 , y = 140)



root.mainloop()