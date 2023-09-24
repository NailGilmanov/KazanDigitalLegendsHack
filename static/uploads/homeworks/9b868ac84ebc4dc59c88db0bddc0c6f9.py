from PIL import Image


def transparency(filename1):
    img1 = Image.open(filename1)
    pixels1 = img1.load()
    x1, y1 = img1.size

    for i in range(x1):
        for j in range(y1):
            r1, g1, b1 = pixels1[i, j]
            pixels1[i, j] = (int(r1 * 0.2 + 255 * 0.8),
                             int(g1 * 0.2 + 255 * 0.8),
                             int(b1 * 0.2 + 255 * 0.8))

    img1.save('2.jpg')


transparency('1.jpeg')
