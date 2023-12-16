from flask import Flask
import random

app = Flask(__name__)


def make_h1_decorator(function):
    def h1_wrapper():
        input_text = function()
        output_text = f"<h1>{input_text}</h1>"
        return output_text
    return h1_wrapper


def insert_start_image_decorator(function):
    def image_wrapper():
        input_html = function()
        add_iframe = ('<iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" '
                      'width="300" height="300" frameBorder="0"</iframe>')
        output_html = f"{input_html}{add_iframe}"
        return output_html
    return image_wrapper


@app.route('/')
@insert_start_image_decorator
@make_h1_decorator
def main_page():
    return 'Guess a number between 0 and 9'

@app.route('/<user_number>')
def user_guest(user_number):
    return user_number


if __name__ == '__main__':
    random_number = random.randint(0, 9)
    app.run(debug=True)

