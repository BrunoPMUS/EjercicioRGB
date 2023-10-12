from gpiozero import LED
import time
puertosalida = 17
lr = LED(puertosalida)

def prender(color)


parpadeando = True
while parpadeando:
    if input("Ingrese el led que se quiere prender 'R','G','B' ").upper == "r":
        lr.on()

    lr.on()
    time.sleep(1)
    lr.off()
    time.sleep(1)