from datetime import datetime
from playsound import playsound

time = input("Enter the time for the alarm in the following format \n HH:MM:SS")  #Input from user
hours = time[0:2]   #Storing hours from user input in variable hours
minutes = time[3:5] #Storing minutes from user input in variable minutes
seconds = time[6:8] #Storing seconds from user input in variable seconds
period = time[9:11].upper()

print("Setting up alarm")

while True:
    today = datetime.now()
    current_hour = today.strftime("%I")    #Extracting at moment's hours
    current_minute = today.strftime("%M")  #Extracting at moment's minutes
    current_seconds = today.strftime("%S") #Extracting at moment's seconds
    current_period = today.strftime("%p")  #Extracting at moment's periods
    if (period == current_period):         #If all units matches then if loop gets executed
        if (hours == current_hour):
            if (minutes == current_minute):
                if (seconds == current_seconds):
                    print("Wake Up!")
                    playsound('alarm.mp3')
                    break
