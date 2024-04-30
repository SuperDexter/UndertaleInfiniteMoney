from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()
sleep(5)


""" Pour qu'il fonctionne tu vas parler à la vendeuse du village des temu et tu execute le code
fais gaffe à bien être sur la première case hein """



vitesse = 0.065
def down():
    keyboard.press(Key.down)
    sleep(vitesse)
    keyboard.release(Key.down)
    sleep(vitesse)




def enter():
    keyboard.press(Key.enter)
    sleep(vitesse)
    keyboard.release(Key.enter)
    print("fini enter!")


def up():
    keyboard.press(Key.up)
    sleep(vitesse)
    keyboard.release(Key.up)
    sleep(vitesse)
def temiobjet():
        
        for i in range(1,17):

             
            keyboard.press(Key.enter)
            sleep(vitesse)
            keyboard.release(Key.enter)
            sleep(vitesse)

        print("fini temi!")

    
def returnmain():
    
    keyboard.press('x')
    sleep(vitesse)
    keyboard.release('x')
    sleep(vitesse)
    print("fini return!")
    sleep(vitesse)

def vendre():
    
    print("début vendre!")
    down()
    for o in range(1,18):
        keyboard.press(Key.enter)
        sleep(vitesse)
        keyboard.release(Key.enter)
        sleep(vitesse)

        
    print("fin vendre!")

    
def farm():


        keyboard.press(Key.enter)
        sleep(vitesse)
        keyboard.release(Key.enter)
        sleep(vitesse)
        down()
        
        temiobjet()
        
        returnmain()
       
        vendre()
        
        up()
        

while True:
    farm()
    