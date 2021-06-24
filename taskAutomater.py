import sys
from threading import currentThread
import webbrowser
import time as time
import datetime
from win10toast_click import ToastNotifier
from time import sleep,localtime,strftime


lab1 = '2162416507'
lab2 = '2162416507'
CompAi = '9436653896'

now = datetime.datetime.now()
day  = now.strftime("%A")

date = datetime.date.today()
date = str(date)
date = date.split('-')
date = int(date[2])

global url

sys.setrecursionlimit(10**9)

def redirect(url):
    webbrowser.open_new_tab(url) 

def RedirectToMeeting(url,directed):

    redirection = lambda : redirect(url)

    if directed == False and url != None:
        title = 'Class starts in 2 mins'

        notification = ToastNotifier()
        notification.show_toast(
            title = title,
            msg = 'Your class starts in 2 mins!\nClick here to be redirected to it',
            icon_path = None,
            duration = 5,
            threaded = False,
            callback_on_click = redirection
        )
        
    directed = True

    seconds = 0
    while seconds < 600:
        time.sleep(1)
        seconds += 1

    if seconds == 600:
        checkDateTime(day)


def checkDateTime(day):

    sleep(1)
    t = localtime()
    time = strftime("%H:%M:%S", t)


    if date >= 1 and date < 8:
        lab1 = '5488765911'
        lab2 = '2687467692'
        CompAi = '4919518419'
    elif date >= 8 and date < 15:
        lab1 = '8436356679'
        lab2  = '5204540518'
        CompAi = '4919518419'
    elif date >= 15 and date < 22:
        lab1 = '3418906817'
        lab2 = '4809487487'
        CompAi = '9436653896'
    elif date >= 22 and date < 29:
        lab1 = '2687467692'
        lab2 = '2348547588'
        CompAi = '9436653896'
    elif date >= 29:
        lab1 = '5488765911'
        lab2 = '2687467692'
        CompAi = '4919518419'

    ids = {'Monday':['5488765911','5458126063','8436356679','4809487487',CompAi],
        'Tuesday':['5488765911','8436356679',lab1,'5204540518','2162416507'],
        'Wednesday':['5488765911','5458126063','8436356679','2348547588','2162416507'],
        'Thursday':['5488765911','5458126063','3418906817',lab2,'2162416507'],
        'Friday':['5204540518','2687467692','4809487487','8436356679','2348547588']
    }

    if time == '08:28:00':
        page_url = 'https://zoom.us/j/5488765911'
        directed = False
        RedirectToMeeting(page_url,directed)
    elif time == '08:38:00':
        page_url = 'https://zoom.us/j/' + ids[day][0]
        directed = False
        RedirectToMeeting(page_url,directed)
    elif time == '09:48:00':
        page_url = 'https://zoom.us/j/' + ids[day][1]
        directed = False
        RedirectToMeeting(page_url,directed)
    elif time == '10:38:00':
        page_url = 'https://zoom.us/j/' + ids[day][2]
        directed = False
        RedirectToMeeting(page_url,directed)
    elif time == '11:28:00':
        page_url = 'https://zoom.us/j/' + ids[day][3]
        directed = False
        RedirectToMeeting(page_url,directed)
    elif time == '12:18:00':
        page_url = 'https://zoom.us/j/' + ids[day][4]
        directed = False
        RedirectToMeeting(page_url,directed)
    else:
        checkDateTime(day)

checkDateTime(day)