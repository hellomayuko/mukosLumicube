# Cherry Tomato
# import time

cube.set_all(black)

pomDuration = 25 #in minutes
secondsInAMinute = 60
durationInSeconds = pomDuration*secondsInAMinute

timeForEachRow = durationInSeconds / 8

numRowFilled = 0

r = 0xC03F3B
w = 0xDABBB4
g = 0x2A683B

top = [
    [0,0,0,0,g,0,0,0],
    [0,0,0,g,g,g,0,0],
    [0,0,r,g,r,g,r,0],
    [0,r,w,w,r,r,r,r],
    [0,r,w,r,r,r,r,r],
    [0,r,r,r,r,r,r,r],
    [0,0,r,r,r,r,r,0],
    [0,0,0,r,r,r,0,0]
]

# Replacing the zeros with black in the "top" list
for row in range(len(top)):
    for col in range(len(top[0])):
        if top[row][col] == 0:
            top[row][col] = black

while(durationInSeconds):
    
    if(durationInSeconds % 2 == 0):
        for i in range(8):
            if(durationInSeconds / timeForEachRow >= abs(i-7)):
                ledsDict = {}
                for c in range(8):
                    ledsDict[(c,i)] = top[abs(i-7)][c]
                cube.set_leds(ledsDict)
                break
    
    elif(durationInSeconds % 1 == 0):
        for i in range(8):
            if(durationInSeconds / timeForEachRow > abs(i-7)):
                ledsDict = {}
                for c in range(8):
                    ledsDict[(c,i)] = black
                cube.set_leds(ledsDict)
                break
    
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