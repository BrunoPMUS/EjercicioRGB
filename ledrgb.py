from gpiozero import LED
import time
puertosalida = 17
lr = LED(puertosalida)

parpadeando = True
while parpadeando:
    input("Ingrese el led que se quiere prender 'R','G','B' ")
    lr.on()
    time.sleep(1)
    lr.off()
    time.sleep(1)