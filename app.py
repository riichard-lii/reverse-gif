from flask import Flask, request
from reverse import reverse_gif

app = Flask(__name__, static_url_path='/static')
# max size 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def home():
    errors = ''
    if request.method == "POST":
        gif_url = None
        try:
            gif_url = request.form['url']
        except:
            errors += 'Something went wrong.\n'
        reverse_gif(gif_url)
        return '''
                <html>
                <head>
                    <title>Result</title>
                    <link rel='icon' href='static/favicon.ico' type='image/x-icon'/>
                </head>
                    <body>
                        <p><img src="static/reversed.gif" alt="reversed-gif"></p>
                        <p><a href="/">Click here to reverse another gif.</a>
                    </body>
                </html>
            '''

    return '''
        <html>
            <head>
                <title>GIF reverser</title>
                <link rel='icon' href='static/favicon.ico' type='image/x-icon'/>
            </head>
            <body>
                {errors}
                <h1>Reverse your Gifs!</h1>
                <p>Enter the URL to GIF:</p>
                <form method="post" action=".">
                    <p><input name="url" /></p>
                    <p><input type="submit" value="Reverse!" /></p>
                    <br>
                    <p>Made by Richard Li @ Northeastern University</p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == "__main__":
    app.run()