from flask import Blueprint, render_template, request, session

bp = Blueprint('community', __name__)

@bp.route('/community')
def community():
    """
    마이 페이지
    """
    return render_template('community.html')