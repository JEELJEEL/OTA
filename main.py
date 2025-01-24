import time
from machine import Pin
p0 = Pin(2, Pin.OUT)
while True:
  p0.on()
  time.sleep_ms(100)
  p0.off()
  time.sleep(2)
