from PIL import Image, ImageDraw



for i in range(1,226):

    last = 225*2

    in_num = "%05d"%i
    out_num = "%05d"%(last-i+1)

    in_path = "img/image-" + in_num + ".jpg"
    out_path = "img/image-" + out_num + ".jpg"

    img = Image.open(in_path)


    # img.show()
    img.save(out_path, quality=100)

    print(in_path)
    print(out_path)
    print("-")



print("Finish!!")
