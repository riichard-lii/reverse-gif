from PIL import Image, ImageSequence
import requests
import os

url_to_gif = input("Enter url to gif: ")
response = requests.get(url_to_gif, stream=True)
img = Image.open(response.raw)
frame_count = img.n_frames
frames = []

for frame in ImageSequence.Iterator(img):
    frames.append(frame.copy())
frames.reverse()

frames[0].save('reversed.gif', format='GIF', append_images=frames[1:], save_all=True, loop=0)
print(os.path.join(os.getcwd(), 'reversed.gif'))