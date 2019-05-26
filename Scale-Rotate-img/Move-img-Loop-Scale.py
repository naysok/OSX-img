
from PIL import Image, ImageDraw


img = Image.open("181025-Desktop-small.png")

print(img.size)

w,h = img.size
print("w :", w)
print("h :", h)



for i in range(0,45):
    num = "%05d"%i
    out_path = "img/image-" + num + ".png"

    scale = i*2

    margin_w = (scale * 1200/750.0)
    margin_h =  scale

    img_resize = img.resize((int(w - margin_w*2), int(h - margin_h*2)), Image.LANCZOS)


    img.paste(img_resize, (int(margin_w), int(margin_h)))

    # img.show()
    img.save(out_path, quality=100)

    print(i)
    print(w, ",", h)


print("Finish!!")

