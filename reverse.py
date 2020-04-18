from PIL import Image
import requests
url_to_gif = input("Enter url to gif: ")
response = requests.get(url_to_gif, stream=True)
img = Image.open(response.raw)
frame_count = img.n_frames
