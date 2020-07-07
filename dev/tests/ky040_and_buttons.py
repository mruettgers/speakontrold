from gpiozero import LED, Button
from signal import pause
from pyky040 import pyky040
import threading

def btn1():
	print("Test1")

def btn2():
	print("Test2")

def btn3():
        print("Test3")

def inc(pos):
	print('+ {}'.format(pos))

def dec(pos):
	print('- {}'.format(pos))

button = Button(pin=14, )
button.when_pressed = btn1
button.when_released = lambda: print ("Released 1")

if button.is_pressed:
	btn1()

button2 = Button(pin=15)
button2.when_pressed = btn2
button2.when_released = lambda: print ("Released 2")

if button2.is_pressed:
	btn2()

button3 = Button(pin=11)
button3.when_pressed = btn3

# Define your callback
def my_callback(scale_position):
    print('Hello world! The scale position is {}'.format(scale_position))

my_encoder = pyky040.Encoder(CLK=10, DT=9)
my_encoder.setup(inc_callback=inc, dec_callback=dec)
#scale_min=0, scale_max=100, step=1, chg_callback=my_callback)
my_thread = threading.Thread(target=my_encoder.watch)
my_thread.start()

pause()
