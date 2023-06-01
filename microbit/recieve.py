from microbit import *
import radio
import os


run = True
radio.config(group=48)
radio.on()
prim = False

file = open("data.txt", "w")
while True:
    if button_a.is_pressed():
        prim = True
    if button_b.is_pressed():
        prim = False
    if prim is True:
        display.show(Image.HAPPY)
        message = radio.receive()
        print(message)
        file.write(message)
    elif prim is False:
        display.show(Image.SAD)
    sleep(100)
    if prim is False and button_b.is_pressed():
        print("WÆÆÆ")
        break
print("DONE")
sleep(323324)
file.close()
print("amgoasa")
