from machine import Pin, ADC, SoftI2C
import ssd1306
import time

# Pin utilizado para el sensor de pulso
HEARTBEAT_PIN = 34

# Configuración del display OLED (128x64)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Función para leer los valores del sensor de pulso
def read_heartbeat():
    return adc_heartbeat.read()

# Inicializar el ADC para leer los valores del sensor de pulso
adc_heartbeat = ADC(Pin(HEARTBEAT_PIN))
adc_heartbeat.atten(ADC.ATTN_11DB)

# Bucle principal
while True:
    # Leer el valor del sensor de pulso
    heartbeat_val = read_heartbeat()

    # Limpiar la pantalla
    oled.fill(0)

    # Imprimir el valor del sensor de pulso en el display OLED
    oled.text("Heartbeat: {}".format(heartbeat_val), 0, 0)

    # Actualizar el display OLED
    oled.show()

    # Esperar un breve período de tiempo antes de volver a leer el valor del sensor
    time.sleep(0.1)

