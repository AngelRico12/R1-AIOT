from machine import Pin
from rotary_irq_esp import RotaryIRQ
import time

pin_clk = 32  # Pin del encoder CLK
pin_dt = 33   # Pin del encoder DT

# Configuración de los pines de los motores
motor1_pin1 = Pin(27, Pin.OUT)
motor1_pin2 = Pin(26, Pin.OUT)
motor2_pin1 = Pin(14, Pin.OUT)
motor2_pin2 = Pin(12, Pin.OUT)


# Inicialización del encoder
encoder = RotaryIRQ(pin_num_clk=pin_clk, pin_num_dt=pin_dt)

# Función para girar los motores dependiendo de la rotación del encoder
def controlar_motores():
    rotacion = encoder.value()
    if rotacion > 0:
        # Girar hacia la derecha
        motor1_pin1.value(1)
        motor1_pin2.value(0)
        motor2_pin1.value(0)
        motor2_pin2.value(1)
    elif rotacion < 0:
        # Girar hacia la izquierda
        motor1_pin1.value(0)
        motor1_pin2.value(1)
        motor2_pin1.value(1)
        motor2_pin2.value(0)
    else:
        # Detener los motores si no hay rotación
        motor1_pin1.value(0)
        motor1_pin2.value(0)
        motor2_pin1.value(0)
        motor2_pin2.value(0)

try:
    while True:
        valor_sensor = encoder.value()
        print("Valor del sensor:", valor_sensor)
        controlar_motores()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
