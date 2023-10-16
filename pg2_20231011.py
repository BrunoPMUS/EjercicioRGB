from gpiozero import LED
import psutil
import time
import random

r = LED(18)
g = LED(14)
b = LED(15)


def parpadear(r):
    r.on()
    time.sleep(1)
    r.off()

def logica(carga):
    
    if carga <= 10:
        g.on()
        time.sleep(5)
        g.off()
    elif carga <= 20:
        b.on()
        time.sleep(5)
        b.off()
    else:
        parpadear(r)
        parpadear(r)


chia = psutil.cpu_percent(1)

while True:
    chia = psutil.cpu_percent(1)
    chia += random.randint(10,30) 
    print(chia)
    logica(chia)
    
    
