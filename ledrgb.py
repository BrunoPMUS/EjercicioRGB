from gpiozero import LED
import time
lr = LED(17)
lg = LED(18)
lb = LED(19)


hola ={
    "r":lr,
    "g":lg,
    "b":lb
}
hola["b"].on


parpadeando = True
while parpadeando:
    if input("Ingrese el led que se quiere prender 'R','G','B' ").upper == "r":
        lr.on()

    lr.on()
    time.sleep(1)
    lr.off()
    time.sleep(1)