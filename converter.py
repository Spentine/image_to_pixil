import base64
import json
import time
from PIL import Image

# generate a unique id starting at 000000
unqid = "000000"
def get_unqid():
    global unqid
    unqid = int(unqid)
    unqid += 1
    unqid = str(unqid)
    while len(unqid) < 6:
        unqid = "0" + unqid
    return unqid

# get parameters
path = input("What is the file name? ")
name = input("What is the name of the image? ")
w, h = Image.open(path).size

# reject large images
if w>1000 or h>1000:
    print("Sorry, your image is too large.")
    exit()
    
# save each frame as an image and then add it to frames
frames = []
with Image.open(path) as gif:
    for i in range(gif.n_frames):
        gif.seek(i)
        gif.save(f"frames/{name}{i}.png")
        with open(f"frames/{name}{i}.png", "rb") as frame:
            encoded = "data:image/pngp98kjasdnasd983/24kasdjasdbase64," + str(base64.b64encode(frame.read()))[2:-1]
        frames.append(
            {
                "name": "",
                "speed": 100,
                "layers": [
                    {
                        "id": 0,
                        "src": encoded,
                        "edit": False,
                        "name": "Background",
                        "opacity": 1,
                        "active": True,
                        "unqid": get_unqid(),
                        "options": {
                            "blend": "source-over",
                            "locked": False,
                            "filter": {
                                "brightness": "100%",
                                "contrast": "100%",
                                "grayscale": "0%",
                                "blur": 0,
                                "hue-rotate": 0,
                                "dropshadow_x": 0,
                                "dropshadow_y": 0,
                                "dropshadow_blur": 0,
                                "dropshadow_alpha": 1
                            }
                        }
                    }
                ],
                "active": True,
                "selectedLayer": 0,
                "unqid": get_unqid(),
                "preview": encoded,
                "width": w,
                "height": h
            }
        )

output = {
    "application": "pixil",
    "type": ".pixil",
    "version": "2.7.0",
    "website": "pixilart.com",
    "author": "https://www.pixilart.com",
    "contact": "support@pixilart.com",
    "width": w,
    "height": h,
    "colors": {
        "palette": [
            "000000",
            "ffffff"
        ]
    },
    "colorSelected": "palette",
    "frames": frames,
    "currentFrame": 0,
    "speed": 100,
    "name": "Untitled",
    "preview": "",
    "previewApp": "",
    "art_edit_id": 0,
    "palette_id": False,
    "created_at": int(time.time()),
    "updated_at": int(time.time()),
    "id": int(time.time())
}

# write data to output file
with open(f'{name}.pixil', 'w') as pixil:
    pixil.write(json.dumps(output, indent=4))

# print encoded image, but maybe don't do this for large files
# print(encoded_original)
print(f".pixil saved in {name}.pixil! Okay bye.")