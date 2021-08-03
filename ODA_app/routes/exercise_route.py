from ODA_app.models.exercise_model import Exercise
from flask import Blueprint, render_template, request, session
from ODA_app.models.exercise_model import Exercise
import random

bp = Blueprint('exercise',__name__)

@bp.route('/exercise')
def exercise():
    """
    운동 추천 페이지
    """
    # exercise_one = Exercise.query.all()
    # recommendate_exercise = random.choice(exercise_one)

    return render_template('exercise.html')#, recommendate_exercise=recommendate_exercise), 200