import time
from machine import Pin
p0 = Pin(0, Pin.OUT)
while True:
  p0.on()
  time.sleep(1)
  p0.off()
  time.sleep(1)
