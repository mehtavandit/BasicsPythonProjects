from tkinter import *
import datetime
import time
import winsound



def alarm(set_alarm_timer):    #Function to set alarm
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()          #Storing current date and time in variablr current_time
        now = current_time.strftime("%H:%M:%S")         #Extracting hours, minutes and seconds
        date = current_time.strftime("%d/%m/%Y")        #Extracting day, month and year
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()         #Line 25, 26, 27, 28, 29 are for GUI
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)


hour = StringVar()    #Variables for setting alarm
min = StringVar()
sec = StringVar()


hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)


submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()


