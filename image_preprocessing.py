from PIL import Image, ImageEnhance

im = Image.open("574480.png")
print(list(im.getdata()))

newimdata = []
for pixel in im.getdata():
    if pixel < 235:
        newimdata.append(0)
    else:
        newimdata.append(255)

newim = Image.new(im.mode, im.size)
newim.putdata(newimdata)
newim = newim.crop((20, 20, 108, 108))

newim.save("bruh.png")
