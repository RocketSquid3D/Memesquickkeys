import board
import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Sets the pi to act as a keyboard
keyboard = Keyboard(usb_hid.devices)

#Button definitions - colors based on initial build, may change during final product
printt_pin = board.GP7  #green
openn_pin = board.GP9   #blue
new_pin = board.GP11   #red
page_pin = board.GP13  #yellow

#Initializing button - "Page" and "Open" buttons are called "Printt" and "Openn" to prevent command confusion
printt = digitalio.DigitalInOut(printt_pin)
printt.direction = digitalio.Direction.INPUT
printt.pull = digitalio.Pull.DOWN

openn = digitalio.DigitalInOut(openn_pin)
openn.direction = digitalio.Direction.INPUT
openn.pull = digitalio.Pull.DOWN

new = digitalio.DigitalInOut(new_pin)
new.direction = digitalio.Direction.INPUT
new.pull = digitalio.Pull.DOWN

page = digitalio.DigitalInOut(page_pin)
page.direction = digitalio.Direction.INPUT
page.pull = digitalio.Pull.DOWN


while True:
    if printt.value:
            print("Print button was pressed")
            keyboard.press(Keycode.COMMAND, Keycode.P)   #These three lines are to initialize the print command
            time.sleep(0.15)
            keyboard.release(Keycode.COMMAND, Keycode.P)
            time.sleep(15)                               #This line is to give "troubleshooting time" for setting reviews and to make sure the printer connects to the ipad.
            keyboard.press(Keycode.ENTER)                #Confirms the print job automatically.
            time.sleep(0.15)
            keyboard.release(Keycode.ENTER)
    if openn.value:
            print("Open Document button was pressed")
            keyboard.press(Keycode.COMMAND, Keycode.O)
            time.sleep(0.15)
            keyboard.release(Keycode.COMMAND, Keycode.O)
    if new.value:
            print("New Document button was pressed")
            keyboard.press(Keycode.COMMAND, Keycode.N) 
            time.sleep(0.15)
            keyboard.release(Keycode.COMMAND, Keycode.N)
    if page.value:
            print("Page Break button was pressed")
            keyboard.press(Keycode.COMMAND, Keycode.ENTER)
            time.sleep(0.15)
            keyboard.release(Keycode.COMMAND, Keycode.ENTER)
    time.sleep(0.1)