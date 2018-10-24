from PIL import Image
from random import randint

img = Image.open("beach.jpg")

img.show() #original image

pixmap = img.load()

def yeahno(filename):
    img = Image.open(filename)
    pixmap = img.load()
    for i in range(0,img.size[0],3):
        for j in range(0,img.size[1],3):
            r, g, b = pixmap[i,j]
            pixmap[i,j] = (r+(randint(0,255)),g+(randint(0,255)),b+(randint(0,255)))
    img.show()
    img.save("yeahno.jpg")
    
    
def deepfry_v1(filename):
    img = Image.open(filename)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            if r >= 127:
                r = 255
            if g >= 127:
                g = 255
            if b >= 127:
                b = 255
            else:
                r = 0
                g = 0
                b = 0
            pixmap[i,j] = (r,g,b)
    img.show()
    img.save("my_deep.jpg")
    
def greyscale(filename):
    img = Image.open(filename)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            avg = int((r + g + b) / 3)
            pixmap[i,j] = (avg,avg,avg)
    img.show()
    img.save("greyscale.jpg")
    
def filter1(filename):
    img = Image.open(filename)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            if r >= 127:
                r = 0
            if g >= 127:
                g = 0
            if b >= 127:
                b = 0
            else:
                r = 255
                g = 255
                b = 255
    img.show()
    
if __name__ == "__main__":
    deepfry_v1("beach.jpg")
    
    
    
#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        r, g, b = pixmap[i,j]
#        
#        r += 100
#        g -= 50
#        b -= 50
#        
#        pixmap[i,j] = (r,g,b)
#        
#img.show()
#
#print(r)
#print(g)
#print(b)