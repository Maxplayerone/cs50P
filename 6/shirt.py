from PIL import Image, ImageOps

def main():
    give_shirt_to("juan.jpg", "betterJuan.jpg")

def give_shirt_to(input, output):
    shirt_image = Image.open("shirt.png")
    shirt_dimensions = (shirt_image.width, shirt_image.height)
    normal_image = Image.open(input)

    normal_image = ImageOps.fit(normal_image, shirt_dimensions)
    normal_image.paste(shirt_image)
    #this thing should work but the shirt is not transparent and it covers Juan :(
    normal_image.save(output, quality=95)
        

if __name__ == "__main__":
    main()