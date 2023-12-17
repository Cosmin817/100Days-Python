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


def insert_low_image_decorator(function):
    def image_wrapper():
        input_html = function()
        add_iframe = ('<img src="https://i.giphy.com/jD4DwBtqPXRXa.webp">')
        output_html = f"{input_html}{add_iframe}"
        return output_html
    return image_wrapper


def insert_high_image_decorator(function):
    def image_wrapper():
        input_html = function()
        add_iframe = ('<img src="https://i.giphy.com/3o6ZtaO9BZHcOjmErm.webp">')
        output_html = f"{input_html}{add_iframe}"
        return output_html
    return image_wrapper


def insert_found_image_decorator(function):
    def image_wrapper():
        input_html = function()
        add_iframe = ('<img src="https://i.giphy.com/4T7e4DmcrP9du.webp">')
        output_html = f"{input_html}{add_iframe}"
        return output_html
    return image_wrapper


@app.route('/')
@insert_start_image_decorator
@make_h1_decorator
def main_page():
    return 'Guess a number between 0 and 9'


@insert_low_image_decorator
@make_h1_decorator
def too_low_content(*args, **kwargs):
    return "<p style='color: red'>Too low, try again !</p>"


@insert_high_image_decorator
@make_h1_decorator
def too_high_content(*args, **kwargs):
    return "<p style='color: purple'>Too high, try again !</p>"


@insert_found_image_decorator
@make_h1_decorator
def right_choice(*args, **kwargs):
    return "<p style='color: green'>You found me!</p>"

@app.route('/<int:user_number>')
def user_guest(user_number):
    int_user_number = int(user_number)
    if int_user_number < random_number:
        content = too_low_content()
        return content
    elif int_user_number > random_number:
        content = too_high_content()
        return content
    elif int_user_number == random_number:
        content = right_choice()
        return content
    else:
        return "Error"


if __name__ == '__main__':
    random_number = random.randint(0, 9)
    print(random_number)
    app.run(debug=True)

