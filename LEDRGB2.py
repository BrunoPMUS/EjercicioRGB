from gpiozero import LED
import time


rojo = LED(1)
azul = LED(2)
verde = LED(3)


def seleccionar_color():
    print("Elige un color:")
    print("1=Rojo")
    print("2=Azul")
    print("3=Verde")
    seleccion = input("Introduce el número del color de LED que deseas encender: ")

    if seleccion == "1":
        return rojo
    elif seleccion == "2":
        return azul
    elif seleccion == "3":
        return verde
    else:
        print("Opción no válida. Introduce 1, 2 o 3.")
        return None

def controlar_led(led):
    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

try:
    color_elegido = seleccionar_color()
    
    if color_elegido is not None:
        print(f"Has elegido el color {color_elegido.pin} ({color_elegido.pin.factory.name}).")
        
        print("¿Quieres que el LED parpadee? (s/n):")
        parpadear = input()

        if parpadear.lower() == "s":
            controlar_led(color_elegido)
        else:
            print(f"El LED {color_elegido.pin} ({color_elegido.pin.factory.name}) está encendido. Presiona Ctrl+C para detener el programa.")

except KeyboardInterrupt:

    color_elegido.off()
