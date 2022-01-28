from PIL import Image
import glob
import os

def convert(arg):
    image = Image.open(arg["img"]).convert("RGB")

    os.remove(arg["img"])

    name = arg["img"].replace("." + arg["from"], "." + arg["to"])

    image.save(name, arg["to"])

def images(arg):
    return glob.glob(arg["path"] + "*." + arg["ext"])

def main():
    path = "C:/Users/stef_/Downloads/"
    imgs = images({
        "path": path,
        "ext": "webp"
    })

    for f in imgs:
        convert({
            "img": f,
            "to": "jpeg",
            "from": "webp",
            "path": path
        })

main()