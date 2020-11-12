import serial
import pyautogui
import time
from pynput.keyboard import Key, Controller
import pydirectinput

pydirectinput.PAUSE = 0.001
pydirectinput.FAILSAFE = True
screen_width, screen_height = pydirectinput.size()

trash_character = 'p'

keyboard = Controller()

serialMoniter = serial.Serial('COM3', 9600, rtscts=True,dsrdtr=True)
time.sleep(3)

print("Ready!")

count = 0

last_character = trash_character

currX = (int) (screen_width/2)
currY = (int) (screen_height/2)
changeX = 60

while(1):
    b = serialMoniter.readline()
    character = b.decode()
    character = character[0:1]
    if(character == last_character):
        continue
   
    keyboard.release(last_character)

    if(character == 'S'):
        keyboard.press('z')
        last_character = 'z'
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
        pydirectinput.moveRel(changeX, 0, 0)
    elif(character == 'W'):
        pydirectinput.moveRel(-changeX, 0, 0)
    else:
        last_character = trash_character
       
   
    count += 1
    time.sleep(0.01)
    if(last_character == 'z'):
        print("release")
        keyboard.release('z')
        last_character = trash_character
        keyboard.press(last_character)
