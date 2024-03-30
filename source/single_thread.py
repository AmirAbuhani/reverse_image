from PIL import Image


# This function will use single thread. it will iterate over each pixel(r,g,b) and reverse it. Finally, the modified
# image will be save at the single_thread_img.jpg.
def single_thread_reverse_img():
    image = Image.open("img1.jpg")
    pix = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            pix[x, y] = ((255 - r), (255 - g), (255 - b))
    image.save("single_thread_img.jpg")
