import serial
import pyautogui
import time
from pynput.keyboard import Key, Controller
import pydirectinput

pydirectinput.PAUSE = 0.001
pydirectinput.FAILSAFE = True
screen_width, screen_height = pydirectinput.size()

trash_character = 'z'

keyboard = Controller()

serialMoniter = serial.Serial('/dev/cu.usbmodem1421', 9600, rtscts=True,dsrdtr=True)
time.sleep(3)

print("Ready!")

count = 0

last_character = trash_character
while(count < 1000):
    b = serialMoniter.readline()
    character = b.decode()
    character = character[0:1]
    if(character == last_character):
        continue
    
    keyboard.release(last_character)
    if(character == 'S'):
        keyboard.press('x')
        last_character = 'x'
    elif(character == 'U'):
        keyboard.press('w')
        last_character = 'w'
    elif(character == 'D'):
        keyboard.press('s')
        last_character = 's'
    elif(character == 'L'):
        keyboard.press('a')
        last_character = 'a'
    elif(character == 'R'):
        keyboard.press('d')
        last_character = 'd'
    elif(character == 'E'):
        pydirectinput.moveTo(screen_width- 1, screen_height/2)
    elif(character == 'W'):
        pydirectinput.moveTo(5, screen_height/2)
    elif(character == 'O'):
        pydirectinput.moveTo(screen_width/2, screen_height/2)
    else:
        last_character = trash_character
        
    
    count += 1
    time.sleep(0.01)
    if(last_character == 'x'):
        print("release")
        keyboard.release('x')
        last_character = trash_character
        keyboard.press(last_character)
