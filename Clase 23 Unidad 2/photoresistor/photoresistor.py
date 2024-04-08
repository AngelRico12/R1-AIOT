from machine import Pin, SoftI2C
import time
import ssd1306

# Definir el pin utilizado para el sensor de luz (fotorresistor)
LIGHT_SENSOR_PIN = 33

# Configuración del display OLED (128x64)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Crear una instancia de Pin para el sensor de luz
light_sensor_pin = Pin(LIGHT_SENSOR_PIN, Pin.IN)

# Bucle principal
while True:
    # Limpiar la pantalla OLED
    oled.fill(0)

    # Leer el estado del pin del sensor de luz
    luz_encendida = light_sensor_pin.value()

    # Mostrar el estado del sensor de luz en la pantalla OLED
    if luz_encendida:
        oled.text("Luz off", 0, 0)
    else:
        oled.text("Luz on", 0, 0)

    # Actualizar el display OLED
    oled.show()

    # Esperar un tiempo antes de realizar otra lectura
    time.sleep(1)
