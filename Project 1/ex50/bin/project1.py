from PIL import Image

def median(theImages):
    listLength = len(theImages)
    sortedValues = sorted(theImages)
    middleIndex = (listLength+1)/2-1
    return sortedValues[middleIndex]

myImage = []

for i in range(1,10):
    myImage.append(Image.open("images/"+ str(i) +".png"))
    
width = 495
height = 557


#for k in range(1,9):
 #   myImage.append(Image.open("images/"+ str(i+1)+".png"))

newImage = Image.new("RGB",((width,height)),color=None)
rPix=[0]*9 
gPix=[0]*9
bPix=[0]*9

for x in range(width):
    for y in range(height):
        for z in range(0,9):#myImage:
            rPix[z], gPix[z], bPix[z] = myImage[z].getpixel((x,y))   #myRed,myGreen,myBlue = Image[z].getpixel((x,y))
        rPix.sort()
        gPix.sort()
        bPix.sort()
            
            #print(myRed)
            
        newImage.putpixel((x,y),(rPix[4], gPix[4], bPix[4]))
newImage.save("NewNew.png")