from gpiozero import LED
import time

lr=LED(puertosalida)
parpadeando = True
while parpadeando:
    lr.on()
    time.sleep(1)
    lr.off()
    time.sleep(1)