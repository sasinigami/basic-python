import pyautogui 
import time 
import PIL 
from PIL import Image, ImageEnhance, ImageFilter 
import pytesseract
import argparse
import cv2
import os

#Take a screenshot of a specific region
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\james.bond\AppData\Local\Tesseract-OCR\tesseract.exe"
time.sleep(5)
pyautogui.screenshot('Outputs/output.png', region=(452,412,1250,550)) #370,318,1300,600

# Resize image
basewidth = 2000 #Adjust this to 2000 or higher
img = Image.open('Outputs/output.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save('Outputs/outputEdited.png')

# load the example image and convert it to grayscale
image = cv2.imread('Outputs/outputEdited.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the image
# if args["preprocess"] == "thresh":
gray = cv2.threshold(gray, 0, 255,
cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
#print(text)

fh = open('hello.txt', 'w')
fh.write(text) 
fh.close() 

# show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)