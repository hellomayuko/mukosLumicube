# Use the button to play jankenpon (rock paper scissors, in Japanese)

import random

cube.set_all(black)

gu =  [[black, black, black, black, black, black, black, black],
                          [black, black, black, black, black, black, black, black],
                          [black, white, blue, white, white, white, white, black],
                          [black, white, blue, white, white, white, white, black],
                          [black, black, white, white, white, white, white, black],
                          [black, black, white, white, white, white, white, black],
                          [black, black, black, black, white, white, white, black],
                          [black, black, black, black, black, black, black, black]]
choki = [[black, black, black, black, black, black, black, black],
                          [black, black, white, black, white, black, black, black],
                          [black, black, white, black, white, black, black, black],
                          [black, black, white, white, white, white, black, black],
                          [black, black, white, white, white, white, black, black],
                          [black, black, blue, white, white, white, white, black],
                          [black, black, black, white, white, white, white, black],
                          [black, black, black, black, black, black, black, black]]

pa = [[black, black, black, black, black, black, black, black],
                          [black, black, white, blue, white, blue, white, black],
                          [black, black, white, blue, white, blue, white, black],
                          [black, black, white, blue, white, blue, white, black],
                          [black, white, white, white, white, white, white, black],
                          [black, white, white, white, white, white, white, black],
                          [black, black, black, black, white, white, white, black],
                          [black, black, black, black, black, black, black, black]]

while True:
    if buttons.top_pressed == 1:
        #JAN
        cube.set_all(green)
        speaker.say("jan")
        
        #KEN
        cube.set_all(yellow)
        speaker.say("ken")
        
        #PON
        cube.set_all(black)
        randNumber = random.randint(0, 2)
        if(randNumber == 0):
            cube.set_panel(0, gu)
            cube.set_panel(1, gu)
            cube.set_panel(2, gu)
        elif(randNumber == 1):
            cube.set_panel(0, choki)
            cube.set_panel(1, choki)
            cube.set_panel(2, choki)
        elif(randNumber == 2):
            cube.set_panel(0, pa)
            cube.set_panel(1, pa)
            cube.set_panel(2, pa)
        speaker.say("pon")
        time.sleep(3)
    else:
        cube.set_all(black)
