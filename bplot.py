from PIL import Image

red = 0 # 0 to 255
green = 0
blue = 0

xLow = -2
xHigh = 1

yLow = -1.5
yHigh = 1.5

image = Image.new("RGB", (1024, 1024))

for y in range(1024):
    zVert = y * ((yHigh - yLow)/(1023)) + yLow

    for x in range(1024):
        zHorz = x * ((xHigh - xLow)/(1023)) + xLow

        z = zHorz + zVert * 1j
        c = z

        for i in range(255):
            if abs(z) > 2:
                break
            z = z * z + c

        image.putpixel((x, y), (i, green, i % 16 * 16))

image.show()
