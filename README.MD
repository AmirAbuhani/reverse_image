Author: Amir Abu Hani

This project examines the performance for image processing task - reverse image in 2 forms:

The first one is when single thread do this task. in this form, one thread go through each pixel that has rgb colors,
and reverse it in this way: (255-r, 255-b, 255-g). Finally, save the result in a single_thread_img.jpg file.
This form(single thread) takes  29.45 seconds for processing.

The second one is when multiple threads do this task. in this form, we check the number of available CPU cores, and this
will be the number of threads. then we divide the image(img1.jpg) into equal chunks, this ensures that each thread
processes an approximately equal portion of the image. Finally, save the result in multi_threads_img.png file.
This form(multiple threads) takes 46.45 seconds for processing.

Note: it is surprising that in single thread it takes less time than multiple thread in this case.
In the first time that I'm run it, the multiple threads takes less time than the single, but then it is the opposite.

