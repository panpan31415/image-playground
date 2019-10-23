from PIL import Image, ImageFilter

# img = Image.open("./Pokedex/pikachu.jpg")
img = Image.open("./Pokedex/astro.jpg")

thumb_img = img.resize((400, 400))

thumb_img.save("thumb.png")


# box = (100, 100, 400, 400)
# region = img.crop(box)

# region.save("save.png", "png")
# filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img.save("blur.png", "png")

# smoothed_img = img.filter(ImageFilter.SMOOTH)
# smoothed_img.save("smooth.png", "png")

# filtered_img.save("blur.png", "png")


# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)

# print(dir(img))
