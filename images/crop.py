from PIL import Image

img = Image.open( 'Banner-chatacter.jpg' )  # size: 2000 x 1549

# out = 1280 * 640
left, top, right, bottom = 0, 0, 2000, 1000
img.show()
cropped = img.crop( ( left, top, right, bottom ) )  # size: 45, 45

# I don't know that the coordinate system marks pixels at their top left corner...
cropped.show()  # IndexError: image index out of range