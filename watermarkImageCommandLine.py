#Import necessary libraries
import sys, random
#Using the Python Image Proccessing library (PIL)
from PIL import Image, ImageFilter, ImageDraw

#Get image name from command line
imageTitle = sys.argv[1]

#open image file and watermark
im = Image.open(imageTitle)
watermark = Image.open('simpleG.png')

#Get size of the image to be watermarked, and the size of the watermark
widthIM, heightIM = im.size
widthW, heightW = watermark.size

#To maintain a consistent watermark, program resizes the watermark image and how many are drawn
#The image to be watermarked will always have 20 of the 'G' watermark on its longer axis
#The number of G's on its shorter axis will adjust dynamically, according to the ratio of the images longer axis/shorter axis

print(widthIM, heightIM)

if(heightIM>widthIM):
	#image is taller then it is wide, number of 'G's on the y axis is 20
	numY = 20
	#number of 'G's on the x axis adjusts dynamically
	numX = ((20*int(widthIM)/int(heightIM)))
	#now set the new dimensions for the watermark
	watermarkNewSize = (heightIM/20)

if (heightIM<=widthIM):
	#image is wider then it is tall, number of 'G's on the x axis is 20
	numX = 20
	#number of 'G's on the x axis adjusts dynamically
	numY = (int(20*heightIM)/int(widthIM))
	#now set the new dimensions for the watermark
	watermarkNewSize = (widthIM/20)

#resize watermark, keep it a square
watermarkResize = watermark.resize((watermarkNewSize, watermarkNewSize))

#now figure out how much to change the position of the watermark each time
positionOffsetToIncrementY = heightIM/numY
positinoOffsetToIncrementX = widthIM/numX

#create a new image to do the transparant watermarking
transparent = Image.new('RGBA', (widthIM, heightIM), (0,0,0,0))

#copy the image to be watermarked to the new image
transparent.paste(im, (0,0))

#watermarking loop, with 2 extra just to be sure
for i in range (0, numX+2):
	for y in range (0, numY+2):
		watermark2 = watermark.rotate(random.randint(0,360))
		transparent.paste(watermarkResize, 
			(((positinoOffsetToIncrementX*i)+random.randint(0,0)),  
				((positionOffsetToIncrementY*y)+random.randint(0,0))), mask=watermarkResize)

#display the watermarked image
transparent.show()

#save the watermarked image
transparent.save('imageWatermarked.png')

