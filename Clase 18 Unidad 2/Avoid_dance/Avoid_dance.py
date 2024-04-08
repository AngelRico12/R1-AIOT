import machine
import time

# Definir el pin del sensor de avoid dance
avoid_sensor_pin = 34

# Definir el pin para controlar el láser
laser_pin = 14
laser = machine.Pin(laser_pin, machine.Pin.OUT)

# Configurar el pin del sensor como entrada
avoid_sensor = machine.Pin(avoid_sensor_pin, machine.Pin.IN)

while True:
    # Leer el estado del sensor
    avoid_sensor_state = avoid_sensor.value()
    
    # Si el sensor detecta algo (cambia a 0), encender el láser
    if avoid_sensor_state == 0:
        print("Objeto detectado - Encendiendo el láser")
        laser.on()
    else:
        print("No hay objeto - Apagando el láser")
        laser.off()
    
    # Esperar un corto período antes de volver a verificar
    time.sleep(0.1)
