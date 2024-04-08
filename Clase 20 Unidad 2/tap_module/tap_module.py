import machine
import time

# Definir el pin del sensor de humedad
humidity_sensor_pin = 34

# Definir los pines del láser
laser_pin_1 = 14
laser_pin_2 = 15
laser_pin_3 = 16

# Configurar los pines del láser como salida
laser_1 = machine.Pin(laser_pin_1, machine.Pin.OUT)
laser_2 = machine.Pin(laser_pin_2, machine.Pin.OUT)
laser_3 = machine.Pin(laser_pin_3, machine.Pin.OUT)

# Función para leer el valor del sensor de humedad
def read_humidity_sensor():
    humidity_value = machine.ADC(machine.Pin(humidity_sensor_pin))
    return humidity_value.read()

# Bucle principal
while True:
    humidity_val = read_humidity_sensor()
    # Determinar si activar el láser basado en el valor del sensor de humedad
    if humidity_val > 500:  # Ajusta este valor según tus necesidades
        # Encender el láser
        laser_1.value(1)
        laser_2.value(1)
        laser_3.value(1)
        print("Humedad alta - Láser activado")
    else:
        # Apagar el láser
        laser_1.value(0)
        laser_2.value(0)
        laser_3.value(0)
        print("Humedad baja - Láser desactivado")
    time.sleep(0.1)  # Pequeña pausa antes de la siguiente lectura del sensor
