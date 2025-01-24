import time
from machine import Pin
p0 = Pin(2, Pin.OUT)
while True:
  p0.on()
  time.sleep(0.5)
  p0.off()
  time.sleep(0.5)
