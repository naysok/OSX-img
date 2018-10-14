from PIL import Image, ImageDraw
import numpy as np

paste_img = Image.open("../src/PS-End.png")
paste_img_resize = paste_img.resize((665, 323), Image.LANCZOS)
mask = paste_img_resize.split()[3]

# start_w = 80
# start_h = 270

random_w_MIN = -300
random_w_MAX = 1380

random_h_MIN = -100
random_h_MAX = 1180



for i in range(44,250):

    in_num = "%05d"%i
    out_num = "%05d"%(i+1)

    in_path = "img/image-" + in_num + ".jpg"
    out_path = "img/image-" + out_num + ".jpg"

    img = Image.open(in_path)


    # w = start_w + i*38
    # h = start_h + i*41

    w = np.random.randint(random_w_MIN, random_w_MAX)
    h = np.random.randint(random_h_MIN, random_h_MAX)

    img.paste(paste_img_resize, (w, h), mask)

    # img.show()
    img.save(out_path, quality=100)

    print(i)
    print(w, ",", h)


print("Finish!!")
