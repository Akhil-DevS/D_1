import datetime
import time
from win10toast import ToastNotifier

def get_time():
    sec=input('intererval between repetition in seconds (in numbers)').strip()
    time_interval=sec
    return(time_interval)

def log(a):
    now= datetime.datetime.now()
    start_time=now.strftime('%H:%M:%S:')
    with open("log.txt",'a')as f:
        f.write(a+str(now)+"\n")

def notify(a):
    notification= ToastNotifier()
    notification.show_toast(a)
    log(a)

def startime(time_interval):
    txt=input("enter reminder txt")
    while(True):
        time.sleep(time_interval)
        notify(txt)

if __name__ == '__main__':
    print('\n\t This program helps to keep repeting reminders')
    time_interval=get_time()
    startime(int(time_interval))





'''data=[1,2,3,4,5,6,7]
print(f'original data{data}')
data.pop(4)
print(f'removing the 5th element {data}')
swap =data[0]
data[0]=data[5]
data[5]=swap
print(f'Replacing 1st and 5th element {data}')'''