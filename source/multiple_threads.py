import os
from PIL import Image
import concurrent.futures


def apply_reverse(pix, width, start_y, end_y):
    for y in range(start_y, end_y):
        for x in range(width):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            pix[x, y] = ((255 - r), (255 - g), (255 - b))


def multiple_threads_reverse_img():
    image = Image.open("img1.jpg")
    pix = image.load()
    width, height = image.size
    # Number of available CPU cores or height of the image
    num_threads = min(os.cpu_count(), height)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Divide the image height into equal chunks
        chunk_size = height // num_threads
        futures = []
        for i in range(num_threads):
            start_y = i * chunk_size
            end_y = (i + 1) * chunk_size if i < num_threads - 1 else height
            futures.append(executor.submit(apply_reverse, pix, width, start_y, end_y))

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    # Save the modified image
    image.save("multi_threads_img.jpg")
