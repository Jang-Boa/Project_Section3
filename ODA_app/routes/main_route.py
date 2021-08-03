from flask import Blueprint, request
from flask.templating import render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    메인 홈페이지
    """
    return render_template('index.html')
