import machine
import time

# Definir el pin del módulo de golpes
temp_module_pin = 34

# Definir el pin del servo
servo_pin = 14
servo_pwm = machine.PWM(machine.Pin(servo_pin), freq=50)

# Función para leer el valor del módulo de golpes
def read_temp_module():
    temp_value = machine.Pin(temp_module_pin, machine.Pin.IN)
    return temp_value.value()

# Función para mover el servo a una posición específica
def move_servo(angle):
    duty = int(40 + (angle / 180) * 115)  # Convertir el ángulo a valor de duty cycle (rango: 40-155)
    servo_pwm.duty(duty)

# Bucle principal
while True:
    temp_val = read_temp_module()  # Llamar a la función read_temp_module()
    # Determinar la acción basada en el valor del módulo de golpes
    if temp_val == 1:  # Se ha detectado un golpe
        print("Temp alta")
        move_servo(0)  # Mover el servo a la posición deseada cuando se detecte un golpe
    else:
        print("Temp baja")
        move_servo(90)  # Mover el servo a la posición central cuando no se detecte un golpe
    time.sleep(0.1)  # Pequeña pausa para suavizar el movimiento
