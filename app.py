from flask import Flask, request
from reverse import reverse_gif

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    errors = ''
    if request.method == "POST":
        gif_url = None
        try:
            gif_url = request.form['url']
        except:
            errors += 'Something went wrong.\n'        
        return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to reverse another gif.</a>
                    </body>
                </html>
            '''.format(result=reverse_gif(gif_url))

    return '''
        <html>
            <body>
                {errors}
                <p>Enter the URL to GIF:</p>
                <form method="post" action=".">
                    <p><input name="url" /></p>
                    <p><input type="submit" value="Reverse!" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == "__main__":
    app.run()