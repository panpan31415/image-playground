import sys
import os
from PIL import Image


# grab first and secind argument

input = None
output = None
if __name__ == "__main__":
    try:
        input = sys.argv[1]
        output = sys.argv[2]
    except IndexError:
        print("folder name needed")

# check is new/exists

if not os.path.exists(output):
    os.makedirs(output)


# loop through entire folder, convert jpg to png, save png to new
for filename in os.listdir(input):
    img = Image.open(f"{input}{filename}")
    img.save(f"{output}{filename.replace('jpg','png')}", "png")
print("all done!")
