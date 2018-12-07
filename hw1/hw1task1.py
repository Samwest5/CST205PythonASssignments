import pickle
import histMachine as hp

# Task 1

with open('imageMatrix','rb') as f:
    mahPickle = pickle.load(f)

with open('homework1.txt','w') as f:
    RGBDict = {'red': [0, 0, 0, 0], 'green': [0, 0, 0, 0], 'blue': [0, 0, 0, 0]}
    for i in mahPickle:
        for j in i:
            for color, value in enumerate(j):
                if color == 0:  # red
                    if 0 <= value <= 63:
                        RGBDict['red'][0] += 1
                    if 64 <= value <= 127:
                        RGBDict['red'][1] += 1
                    if 128 <= value <= 191:
                        RGBDict['red'][2] += 1
                    if 192 <= value <= 255:
                        RGBDict['red'][3] += 1
                if color == 1:  # green
                    if 0 <= value <= 63:
                        RGBDict['green'][0] += 1
                    if 64 <= value <= 127:
                        RGBDict['green'][1] += 1
                    if 128 <= value <= 191:
                        RGBDict['green'][2] += 1
                    if 192 <= value <= 255:
                        RGBDict['green'][3] += 1
                if color == 2:  # blue
                    if 0 <= value <= 63:
                        RGBDict['blue'][0] += 1
                    if 64 <= value <= 127:
                        RGBDict['blue'][1] += 1
                    if 128 <= value <= 191:
                        RGBDict['blue'][2] += 1
                    if 192 <= value <= 255:
                        RGBDict['blue'][3] += 1
    f.write(str(RGBDict))


redList = []
greenList = []
blueList = []

for i in mahPickle:
    for j in i:
        for color, value in enumerate(j):
            if color == 0:
                redList.append(value)
            if color == 1:
                greenList.append(value)
            if color == 2:
                blueList.append(value)






hp.hist_plotter(redList, greenList, blueList)






































