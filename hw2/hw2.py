# CST 205
# Sam Westigard
# 2/2018
# median filter

from PIL import Image
import glob

imageList = glob.glob('images/*.png')

for i in range(len(imageList)):
    imageList[i] = Image.open(imageList[i])

filteredImage = Image.new('RGB', (imageList[0].width, imageList[0].height), 'white')

def medianColor(imageList, x, y):

    redList = []
    greenList = []
    blueList = []

    for i in imageList:
        redList.append(i.getpixel((x, y))[0])
        greenList.append(i.getpixel((x, y))[1])
        blueList.append(i.getpixel((x, y))[2])

    redList.sort()
    greenList.sort()
    blueList.sort()

    medianRed = redList[int((len(redList) + 1) / 2 + - 1)]
    medianGreen = greenList[int((len(greenList) + 1) / 2 - 1)]
    medianBlue = blueList[int((len(blueList) + 1) / 2 - 1)]

    return (medianRed, medianGreen, medianBlue)

for x in range(filteredImage.width):
    for y in range(filteredImage.height):
        filteredImage.putpixel((x, y), medianColor(imageList, x, y))

filteredImage.save('filtered.png')




















