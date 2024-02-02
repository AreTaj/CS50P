# CS50 P-Shirt
# Problem Set 6

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    # Open image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open shirt
    shirtfile = Image.open("shirt.png")
    # Shirt size
    size = shirtfile.size
    # Resize muppet image to fit
    muppet = ImageOps.fit(imagefile, size)
    # Paste shirt in muppet
    muppet.paste(shirtfile, shirtfile)
    # Create outpit file
    muppet.save(sys.argv[2])


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments.")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments.")

    file1 = splitext(sys.argv[1])   # Before
    file2 = splitext(sys.argv[2])   # After

    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extension(file):
    if file in [".jpeg", ".jpg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()