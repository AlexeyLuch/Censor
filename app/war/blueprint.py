from flask import Blueprint, render_template

war = Blueprint('war', __name__, template_folder="templates")

@war.route('/')
def index():
    return render_template('war/index.html')