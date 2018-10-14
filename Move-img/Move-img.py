from PIL import Image, ImageDraw

paste_img = Image.open("../src/PS-End.png")
paste_img_resize = paste_img.resize((665, 323), Image.LANCZOS)
mask = paste_img_resize.split()[3]

start_w = 80
start_h = 270



for i in range(0,20):

    in_num = "%05d"%i
    out_num = "%05d"%(i+1)

    in_path = "img/image-" + in_num + ".jpg"
    out_path = "img/image-" + out_num + ".jpg"

    img = Image.open(in_path)

    w = start_w + i*38
    h = start_h + i*41

    img.paste(paste_img_resize, (w, h), mask)

    # img.show()
    img.save(out_path, quality=100)

    print(i)
    print(w, ",", h)


print("Finish!!")
