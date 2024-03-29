#Created by Ansh Jain(AJking)

from tkinter import *
import random


#Create Main Window
root = Tk()
#Create Title and geometry of the window
root.title("Welcome to my game!")
root.geometry("1000x700")

#Greeting Title
greeting = Label(
    text="Greetings! Human       Select truth or dare",
    fg="black",
    bg="SeaGreen1",
    width="1000",
    height="3",
    font="arial, 9" )

#pack and deploy the greeting title
greeting.pack()

frame = LabelFrame(root, padx=10, pady=10)

#truths and dare
truths = ['What is your worst habit?', 'Do you sing in the shower?', 'Are you scared of the dark?', 'Are you a bitch?', 'Tell us your Girlfriends/Boyfriends name.', 'Who is your crush?', 'You are safe', 'who is your favorite here', 'Do you want a daughter or a son', 'Are you gay', 'Are you happy']
dare = ['Dance in the street like crazy.', 'Bark like a dog loudly.', 'take your shirt off spin it.', 'Slap your self and dance', 'Say a swear word to your best friend', 'You are safe']

#set up commands for the buttons
def btn_truth():
    b1 = Label(text=random.choice(truths))
    b1.pack()

def btn_dare():
    b2 = Label(text=random.choice(dare))
    b2.pack()
    
#set up buttons   
truth = Button(frame, text="Truth", borderwidth=0, command=btn_truth, font="arial, 15")
dare1 = Button(frame, text="Dare", borderwidth=0, command=btn_dare, font="arial, 15")
exit= Button(frame, text="EXIT", borderwidth=0, command=root.destroy, fg="red", font="arial, 17")

#pack the buttons
truth.pack(side="left", padx=100)
dare1.pack(side="right", padx=100)
exit.pack(side="bottom")

frame.pack()

#Loop the window
root.mainloop()
