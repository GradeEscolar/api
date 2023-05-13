from flask import Blueprint, render_template

controller = Blueprint('home_controler', __name__, template_folder='./templates')

@controller.get('/')
def get():
    return render_template('home_template.html')