# Example for micropython.org device, gpio mode
# Connections:
# Pin # | HX711
# ------|-----------
# 12    | data_pin
# 13    | clock_pin
#

from hx711_gpio_one import HX711
from machine import Pin
import time

pin_OUT = Pin(12, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(13, Pin.OUT)

hx711 = HX711(pin_SCK, pin_OUT)

hx711.tare()
hx711.set_scale(-420.5)

while (True):
   # value = hx711.read()

  #  value = hx711.get_value()
    
    units = hx711.get_units()
    
    time.sleep(0.5)

  #  print(value)
    print(units)
