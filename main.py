from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

URL = 'https://api.npoint.io/c790b4d5cab58020d391'
request = requests.get(URL)
request.raise_for_status()

request_posts_data = request.json()


@app.route('/')
def home_page():
    return render_template('index.html', posts_headlines=request_posts_data)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post_page(post_id: int):
    correct_data = "NULL"
    for mydict in request_posts_data:
        if int(mydict['id']) == post_id:
            correct_data = mydict
    return render_template('post.html', post=correct_data)

@app.route("/form-entry")
def receive_data():
    return "<h1>receive_data is here</h1>"


if __name__ == '__main__':
    app.run(debug=True)
