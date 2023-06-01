from microbit import *
import radio
run = True
radio.config(group=48)
radio.on()
while True:
    display.show(Image.HAPPY)
    sleep(20)
    radio.send(str(accelerometer.get_values()))
