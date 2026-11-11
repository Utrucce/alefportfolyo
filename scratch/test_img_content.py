from PIL import Image

p = r"C:\Users\pc\Desktop\alef-privacy-site\assets\book_utrucce.jpg"
im = Image.open(p)
print("Format:", im.format, "Size:", im.size, "Mode:", im.mode)
# get some pixel info or crop
print("Colors in top left:", im.getpixel((10, 10)))
print("Colors in center:", im.getpixel((im.width//2, im.height//2)))
