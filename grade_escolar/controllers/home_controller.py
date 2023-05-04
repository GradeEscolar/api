from flask import Blueprint, render_template

blueprint = Blueprint('home_controler', __name__, template_folder='./templates')

@blueprint.route('/')
def get():
    return render_template('home_template.html')