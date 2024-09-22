import base64
import json
import time
from PIL import Image

# get parameters
path = input("What is the file path? ")
name = input("What is the name of the image? ")
w, h = Image.open(path).size

if w>1000 or h>1000:
    print("Sorry, your image is too large.")
    exit()

# encode image in base64
with open(path, "rb") as image:
    encoded_original = str(base64.b64encode(image.read()))[2:-1]
    encoded = "data:image/pngp98kjasdnasd983/24kasdjasdbase64," + encoded_original

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
    "frames": [
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
                    "unqid": "blabla",
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
            "unqid": "blablo",
            "preview": "data:image/pngp98kjasdnasd983/24kasdjasdbase64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABkCAYAAAAR+rcWAAAAAXNSR0IArs4c6QAAA2lJREFUeF7tnVlywjAQBcVlkvsfh1yGlB1MhNAym/aXH4pCELvdMyPJtnxzzn05537wKuNwc39/gCiU6AAIeEJ4R+TCQAW8Qz4YqIxAGAgD++ZwGAgDYeDUnXhUYVThvsNQGAgDYeAxFr8/JzU4L98jzCL16gc+fFKPt3c0hrdry/+bd0lHLf/pC5MEWAlrALTZfrUw8AzPGtBSUD2Y1cO85pE6jWsJLgTqgay2nzUMbG4cI7zNjbQ+MveexhFBmkK0MrB7uJbgXZ9bh7WFgY+RrSsUGvX+aw2cEl5gowqi5stTw7OCKDVwCXgWECUGLgVPC5Fr4JLwNBA5Bi4NTwqRauAW8CQQqQYOPcKgdqKp7Z6dbdKIhWLgVvACC4sQKQZuFb7cMC4ZuCU8DsScgVvDo0LMGbhl7ktMyiZzYXMDjwo30+zNsyInOaUMRPh6KuYgpsgifD8BRsN4WQMtUwXXQIRvZMiSghgzEOGbBvgRxrEcCANhIHXagN4uNcEQGojwzTCNQQxzIMK3DPBNOhhIj2IHAxmwYk1jXRmVgZadVeW+Nfm6uYGbArTLgZsCfOtMq6vwThDNc+CReDYEaGvgThCrGOifO5hppllStilV+LzpRQJi9VCmjoWPW0/Fw7mVITabD1wVYhMDV86HHANVYbwiRO45EXEhSZyUnuo8cGYSod9ZuZHzImXbJAaahLF/NCkbKumbab9T2i7plQlmYRxCPN5L+plaUNL0kqq+183eza+NuYZ+1w61hvkEQj6IGgPNwziToM+PasLkgvMOdPYi1KGuUL120spO//e4B6dk3rXuYukK1Sq5kJrPQqDU71kcgFLuo+RAf2VL0QQDd4dHaU+Fx1nBUjzBMAoUznZQw5e7guUWEDnwOAZe4bw0RC48roFLQ5TAkxi4JEQpPKmBS0HUwNMYuARELTytgVNDtIBnYeALYu2xLKcfl2vrjW4ow9jiMvkmP+Kt4zf0iIUzwqA+Y4AyFuausou1s4xWhuy+HJR1uMa41DAwNLa5kR644h3nWlmsc2Au3LGCJTWxEtphDVUCpGIXwK/egm5K9fCkhHeLHMit4lO1b5kDOUZOAxEG4nkieJ7INOEaK5zIgXiaA57mMHV1RhVGFUYVRhWmjBmNx87DQEcORA5EDhwmHCVp5hceTG5JJYZbdAAAAABJRU5ErkJggg==",
            "width": w,
            "height": h
        }
    ],
    "currentFrame": 0,
    "speed": 100,
    "name": "Untitled",
    "preview": "data:image/pngp98kjasdnasd983/24kasdjasdbase64,iVBORw0KGgoAAAANSUhEUgAAAFAA/sfR5H8Fkddasdmnacvx/AABkCAYAAAAR+rcWAAAAAXNSR0IArs4c6QAAA2lJREFUeF7tnVlywjAQBcVlkvsfh1yGlB1MhNAym/aXH4pCELvdMyPJtnxzzn05537wKuNwc39/gCiU6AAIeEJ4R+TCQAW8Qz4YqIxAGAgD++ZwGAgDYeDUnXhUYVThvsNQGAgDYeAxFr8/JzU4L98jzCL16gc+fFKPt3c0hrdry/+bd0lHLf/pC5MEWAlrALTZfrUw8AzPGtBSUD2Y1cO85pE6jWsJLgTqgay2nzUMbG4cI7zNjbQ+MveexhFBmkK0MrB7uJbgXZ9bh7WFgY+RrSsUGvX+aw2cEl5gowqi5stTw7OCKDVwCXgWECUGLgVPC5Fr4JLwNBA5Bi4NTwqRauAW8CQQqQYOPcKgdqKp7Z6dbdKIhWLgVvACC4sQKQZuFb7cMC4ZuCU8DsScgVvDo0LMGbhl7ktMyiZzYXMDjwo30+zNsyInOaUMRPh6KuYgpsgifD8BRsN4WQMtUwXXQIRvZMiSghgzEOGbBvgRxrEcCANhIHXagN4uNcEQGojwzTCNQQxzIMK3DPBNOhhIj2IHAxmwYk1jXRmVgZadVeW+Nfm6uYGbArTLgZsCfOtMq6vwThDNc+CReDYEaGvgThCrGOifO5hppllStilV+LzpRQJi9VCmjoWPW0/Fw7mVITabD1wVYhMDV86HHANVYbwiRO45EXEhSZyUnuo8cGYSod9ZuZHzImXbJAaahLF/NCkbKumbab9T2i7plQlmYRxCPN5L+plaUNL0kqq+183eza+NuYZ+1w61hvkEQj6IGgPNwziToM+PasLkgvMOdPYi1KGuUL120spO//e4B6dk3rXuYukK1Sq5kJrPQqDU71kcgFLuo+RAf2VL0QQDd4dHaU+Fx1nBUjzBMAoUznZQw5e7guUWEDnwOAZe4bw0RC48roFLQ5TAkxi4JEQpPKmBS0HUwNMYuARELTytgVNDtIBnYeALYu2xLKcfl2vrjW4ow9jiMvkmP+Kt4zf0iIUzwqA+Y4AyFuausou1s4xWhuy+HJR1uMa41DAwNLa5kR644h3nWlmsc2Au3LGCJTWxEtphDVUCpGIXwK/egm5K9fCkhHeLHMit4lO1b5kDOUZOAxEG4nkieJ7INOEaK5zIgXiaA57mMHV1RhVGFUYVRhWmjBmNx87DQEcORA5EDhwmHCVp5hceTG5JJYZbdAAAAABJRU5ErkJggg==",
    "previewApp": "",
    "art_edit_id": 0,
    "palette_id": "64630",
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