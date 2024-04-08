from machine import Pin, I2C
import ssd1306
import time

# Configuración de pines para el joystick
X_PIN = 34
Y_PIN = 35
BUTTON_PIN = 32

# Configuración del display OLED (128x64)
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Función para leer los valores del joystick
def read_joystick():
    x = adc_x.read()
    y = adc_y.read()
    button = button_pin.value()
    return x, y, button

# Inicializar el ADC para leer los valores del joystick
adc_x = ADC(Pin(X_PIN))
adc_x.atten(ADC.ATTN_11DB)
adc_y = ADC(Pin(Y_PIN))
adc_y.atten(ADC.ATTN_11DB)
button_pin = Pin(BUTTON_PIN, Pin.IN)

# Bucle principal
while True:
    # Leer los valores del joystick
    x_val, y_val, button_val = read_joystick()

    # Limpiar la pantalla
    oled.fill(0)

    # Imprimir los valores en el display OLED
    oled.text("Joystick Values:", 0, 0)
    oled.text("X: {}".format(x_val), 0, 16)
    oled.text("Y: {}".format(y_val), 0, 32)
    oled.text("Button: {}".format(button_val), 0, 48)

    # Actualizar el display OLED
    oled.show()

    # Esperar un breve período de tiempo antes de volver a leer los valores
    time.sleep(0.1)
