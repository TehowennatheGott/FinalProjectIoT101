#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    May 08, 2023 01:33:10 AM EDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import RPi.GPIO as GPIO
import time
from datetime import datetime
import ADC0832
import sys


global moisture
global WaterDate


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

buttonRED = 3
buttonBLUE = 5

ledGood= 38
ledBad = 40
waterFan = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(buttonRED, GPIO.IN,pull_up_down = GPIO.PUD_UP )
GPIO.setup(buttonBLUE, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ledGood, GPIO.OUT)
GPIO.output(ledGood,GPIO.LOW)
GPIO.setup(ledBad, GPIO.OUT)
GPIO.output(ledBad,GPIO.LOW)
GPIO.setup(waterFan, GPIO.OUT)
GPIO.output(waterFan,GPIO.LOW)



class Toplevel1:
    def __init__(self, top=None):#boilerplate GUI work
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x589+1144+190")#boilerplate GUI work
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Gardening Tool")

        self.top = top

        self.Label1 = tk.Label(self.top)#boilerplate GUI work
        self.Label1.place(relx=0.017, rely=0.022, height=28, width=119)
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''Last Water Date''') #label for last watering date
        
        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.017, rely=0.445, height=27, width=129)
        self.Label4.configure(anchor='w')
        self.Label4.configure(compound='left')
        self.Label4.configure(text='''Current Moisture''') #label for current moisture
        
        self.waterdatelabel = tk.Label(self.top)
        self.waterdatelabel.place(relx=0.017, rely=0.066, height=28, width=399)
        self.waterdatelabel.configure(anchor='w')
        self.waterdatelabel.configure(compound='left') #label for text
        
        self.moistlabel = tk.Label(self.top)
        self.moistlabel.place(relx=0.017, rely=0.489, height=28, width=449)
        self.moistlabel.configure(anchor='w')
        self.moistlabel.configure(compound='left') #label for text
        
        self.healthbutton = tk.Button(self.top)
        self.healthbutton.place(relx=0.583, rely=0.467, height=33, width=103)
        self.healthbutton.configure(activebackground="beige")
        self.healthbutton.configure(borderwidth="2")
        self.healthbutton.configure(compound='left')
        self.healthbutton.configure(text='''Check Health''')
        self.healthbutton.configure(command=self.Start) #runs Start()
        
        self.planttypelabel = tk.Label(self.top)
        self.planttypelabel.place(relx=0.567, rely=0.044, height=28, width=199)
        self.planttypelabel.configure(anchor='w')
        self.planttypelabel.configure(compound='left')
        self.planttypelabel.configure(cursor="fleur")
        self.planttypelabel.configure(text='''Your plant is: A tomato''') #
        
        self.planthealthlabel = tk.Label(self.top)
        self.planthealthlabel.place(relx=0.567, rely=0.17, height=28, width=209)
        self.planthealthlabel.configure(anchor='w')
        self.planthealthlabel.configure(compound='left')
        self.planthealthlabel.configure(cursor="fleur")
        self.planthealthlabel.configure(text='''your plant needs:''')
        
        self.waterbutton = tk.Button(self.top)
        self.waterbutton.place(relx=0.583, rely=0.56, height=33, width=103)
        self.waterbutton.configure(activebackground="beige")
        self.waterbutton.configure(borderwidth="2")
        self.waterbutton.configure(compound='left')
        self.waterbutton.configure(text='''Water''')
        self.waterbutton.configure(command=self.Water)
        
    def Start(self):
        global WaterDate
        global moisture
        res = ADC0832.getResult()
        moisture = 255 - res
        print(moisture)
        newwater=str(WaterDate)
        newmoist = str(moisture)
        self.waterdatelabel['text'] = f"{newwater}"
        self.moistlabel['text'] = f"{newmoist}"
        
    def Water(self):
        print("pog")
        global WaterDate
        WaterDate = datetime.now()#change water date to now
        GPIO.output(waterFan, GPIO.HIGH)
        time.sleep(4)
        print(WaterDate)
        
        

def main(*args):# entry point for the GUI of the program
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Toplevel1(_top1)
    root.mainloop()
    
       
def moistTF():
    global moisture
    res = ADC0832.getResult()
    moisture = 255 - res
    print(moisture)
    print("Res:",res)
    if moisture > 30 and moisture < 200:
        GPIO.output(ledBad,GPIO.HIGH)#steady for good
        time.sleep(2)#turn on the alert for 2 seconds
        GPIO.output(ledBad,GPIO.LOW)
    else:
        GPIO.output(ledBad,GPIO.HIGH)#blink if bad
        time.sleep(1)#turn on the alert for 1 second
        GPIO.output(ledBad,GPIO.LOW)
        time.sleep(1)#turn on the alert for 1 second
        GPIO.output(ledBad,GPIO.HIGH)#blink if bad
        time.sleep(1)#turn on the alert for 1 second
        GPIO.output(ledBad,GPIO.LOW)
        time.sleep(1)#turn on the alert for 1 second
        GPIO.output(ledBad,GPIO.HIGH)#blink if bad
        time.sleep(1)#turn on the alert for 1 second
        GPIO.output(ledBad,GPIO.LOW)
        
        
def GetStats(channel):
    moistTF()

def careandWater(channel):
    global WaterDate
    WaterDate = datetime.now()#change water date to now
    GPIO.output(waterFan, GPIO.HIGH)
    time.sleep(4)#turn on the water motor for 4 seconds
    GPIO.output(waterFan, GPIO.LOW)
    print(WaterDate)
    
GPIO.add_event_detect(buttonRED,GPIO.FALLING,callback=GetStats)
GPIO.add_event_detect(buttonBLUE,GPIO.FALLING,callback=careandWater)




try:
    ADC0832.setup()
    print("running...")
    while True:
        if (len(sys.argv)) > 1:
            main()
        pass
except KeyboardInterrupt:
    GPIO.cleanup()




