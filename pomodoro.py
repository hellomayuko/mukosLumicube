# Cherry Tomato
# import time

cube.set_all(black)

pomDuration = 25 #in minutes
secondsInAMinute = 60
durationInSeconds = pomDuration*secondsInAMinute

timeForEachRow = durationInSeconds / 8

numRowFilled = 0

#     [0,0,0,0,g,0,0,0],
#     [0,0,0,g,g,g,0,0],
#     [0,0,r,g,r,g,r,0],
#     [0,r,w,w,r,r,r,r],
#     [0,r,w,r,r,r,r,r],
#     [0,r,r,r,r,r,r,r],
#     [0,0,r,r,r,r,r,0],
#     [0,0,0,r,r,r,0,0],

r = 0xC03F3B
w = 0xDABBB4
g = 0x2A683B

while(durationInSeconds):
    
    if(durationInSeconds % 2 == 0):
        if(durationInSeconds / timeForEachRow >= 7):
            cube.set_leds({(0,0): black,
            (1,0): black,
            (2,0): black,
            (3,0): r,
            (4,0): r,
            (5,0): r,
            (6,0): black,
            (7,0): black})
        elif(durationInSeconds / timeForEachRow >= 6):
            cube.set_leds({(0,1): black,
            (1,1): black,
            (2,1): r,
            (3,1): r,
            (4,1): r,
            (5,1): r,
            (6,1): r,
            (7,1): black})
        elif(durationInSeconds / timeForEachRow >= 5):
            cube.set_leds({(0,2): black,
            (1,2): r,
            (2,2): r,
            (3,2): r,
            (4,2): r,
            (5,2): r,
            (6,2): r,
            (7,2): r})
        elif(durationInSeconds / timeForEachRow >= 4):
            cube.set_leds({(0,3): black,
            (1,3): r,
            (2,3): w,
            (3,3): r,
            (4,3): r,
            (5,3): r,
            (6,3): r,
            (7,3): r})
        elif(durationInSeconds / timeForEachRow >= 3):
            cube.set_leds({(0,4): black,
            (1,4): r,
            (2,4): w,
            (3,4): w,
            (4,4): r,
            (5,4): r,
            (6,4): r,
            (7,4): r})
        elif(durationInSeconds / timeForEachRow >= 2):
            cube.set_leds({(0,5): black,
            (1,5): black,
            (2,5): r,
            (3,5): g,
            (4,5): r,
            (5,5): g,
            (6,5): r,
            (7,5): black})
        elif(durationInSeconds / timeForEachRow >= 1):
            cube.set_leds({(0,6): black,
            (1,6): black,
            (2,6): black,
            (3,6): g,
            (4,6): g,
            (5,6): g,
            (6,6): black,
            (7,6): black})
        elif(durationInSeconds / timeForEachRow >= 0):
            cube.set_leds({(0,7): black,
            (1,7): black,
            (2,7): black,
            (3,7): black,
            (4,7): g,
            (5,7): black,
            (6,7): black,
            (7,7): black})
        
        
    elif(durationInSeconds % 1 == 0):
        if(durationInSeconds / timeForEachRow > 7):
            cube.set_leds({(0,0): black,
            (1,0): black,
            (2,0): black,
            (3,0): black,
            (4,0): black,
            (5,0): black,
            (6,0): black,
            (7,0): black})
        elif(durationInSeconds / timeForEachRow > 6):
            cube.set_leds({(0,1): black,
            (1,1): black,
            (2,1): black,
            (3,1): black,
            (4,1): black,
            (5,1): black,
            (6,1): black,
            (7,1): black})
        elif(durationInSeconds / timeForEachRow > 5):
            cube.set_leds({(0,2): black,
            (1,2): black,
            (2,2): black,
            (3,2): black,
            (4,2): black,
            (5,2): black,
            (6,2): black,
            (7,2): black})
        elif(durationInSeconds / timeForEachRow > 4):
            cube.set_leds({(0,3): black,
            (1,3): black,
            (2,3): black,
            (3,3): black,
            (4,3): black,
            (5,3): black,
            (6,3): black,
            (7,3): black})
        elif(durationInSeconds / timeForEachRow > 3):
            cube.set_leds({(0,4): black,
            (1,4): black,
            (2,4): black,
            (3,4): black,
            (4,4): black,
            (5,4): black,
            (6,4): black,
            (7,4): black})
        elif(durationInSeconds / timeForEachRow > 2):
            cube.set_leds({(0,5): black,
            (1,5): black,
            (2,5): black,
            (3,5): black,
            (4,5): black,
            (5,5): black,
            (6,5): black,
            (7,5): black})
        elif(durationInSeconds / timeForEachRow > 1):
            cube.set_leds({(0,6): black,
            (1,6): black,
            (2,6): black,
            (3,6): black,
            (4,6): black,
            (5,6): black,
            (6,6): black,
            (7,6): black})
        elif(durationInSeconds / timeForEachRow > 0):
            cube.set_leds({(0,7): black,
            (1,7): black,
            (2,7): black,
            (3,7): black,
            (4,7): black,
            (5,7): black,
            (6,7): black,
            (7,7): black})
    
    
    time.sleep(1)
    durationInSeconds -= 1

cube.scroll_text("Yooooooo", green)

# Sets all LEDs to a lil cherry tomato
# r = 0xC03F3B
# w = 0xDABBB4
# g = 0x2A683B
# top = [
#     [0,0,0,0,g,0,0,0],
#     [0,0,0,g,g,g,0,0],
#     [0,0,r,g,r,g,r,0],
#     [0,r,w,w,r,r,r,r],
#     [0,r,w,r,r,r,r,r],
#     [0,r,r,r,r,r,r,r],
#     [0,0,r,r,r,r,r,0],
#     [0,0,0,r,r,r,0,0],
# ]