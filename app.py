from flask import Flask, request, render_template
from reverse import reverse_gif
from django.core.exceptions import ValidationError

app = Flask(__name__, static_url_path='/static')
# max size 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    errors = ''
    if request.method == "POST":
        gif_url = request.form['url']
        try:
            reverse_gif(gif_url)
            return render_template('result.html')
        except ValidationError:
            return render_template('error.html', msg= gif_url + ' is not a valid URL/GIF!')
        except ValueError:
            return render_template('error.html', msg='The file is too big!')
    return render_template('home.html')

if __name__ == "__main__":
    app.run()