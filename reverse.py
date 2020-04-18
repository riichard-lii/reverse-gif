from PIL import Image, ImageSequence
import requests
import os
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def reverse_gif(url_to_gif):
    val = URLValidator()
    val(url_to_gif)
    if not url_to_gif.endswith('.gif'):
        raise ValidationError
    response = requests.head(url_to_gif, stream=True)

    if int(response.headers['Content-Length']) > 10000000:
        print('too big')
        return ''
    response = requests.get(url_to_gif, stream=True)
    img = Image.open(response.raw)
    frame_count = img.n_frames
    frames = []
    for frame in ImageSequence.Iterator(img):
        frames.append(frame.copy())
    frames.reverse()
    frames[0].save(os.path.join('static', 'reversed.gif'), format='GIF', append_images=frames[1:], save_all=True, loop=0)
    return os.path.join(os.getcwd(), 'static', 'reversed.gif')

if __name__ == "__main__":
    reverse_gif(input("Enter url to gif: "))