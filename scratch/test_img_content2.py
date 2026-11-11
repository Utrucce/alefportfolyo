from PIL import Image

p = r"C:\Users\pc\Desktop\alef-privacy-site\assets\book_cover_7RdaEQAAQBAJ.jpg"
im = Image.open(p)
print("Format:", im.format, "Size:", im.size, "Mode:", im.mode)
print("Colors in top left:", im.getpixel((10, 10)))
print("Colors in center:", im.getpixel((im.width//2, im.height//2)))
