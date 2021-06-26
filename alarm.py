from tkinter import *
import time
import datetime
from win10toast import ToastNotifier
import winsound

def alarm(set_time):
    while(True):
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if(now==set_time):
            noti=ToastNotifier()
            noti.show_toast("Time to wake up")
            winsound.Playsound('sound.waw',winsound.SND_ASYNC)
            break

def get_time():
    set_time= f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_time)

clock=Tk()
clock.title("ALARM CLOCK")
clock.geometry(400*400)
time_format=Label(clock,text="enter time in 24hrs")
fg="red",bg="black",font="Arial".place(x=70,y=130)
addtime=Label(clock,text='Hour Min Sec',font=60).place(x=120)
set_alarm=Label(clock,text='alarm time',fg='blue',bg='red',relif='solid',font=('helevetica',7,'bold')).place(x=0,y=29)
hour=StringVar()
min=StringVar()
sec=StringVar()




