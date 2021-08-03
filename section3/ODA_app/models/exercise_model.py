from ODA_app import db

class Exercise(db.Model):
    """
    운동 관련 유튜브 영상 테이블
    """
    __tablename__ = 'exercise'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    youtube_url = db.Column(db.String(400),nullable=False)
    body_id = db.Column(db.Integer,db.ForeignKey('body.id',ondelete='CASCADE'),nullable=False)
    time = db.Column(db.Float,nullable=False)
    # body = db.relationship('Body', backref=db.backref('exercise_set'))

    def __repr__(self):
        return f"Exercise: {self.id}"


class Body(db.Model):
    """
    운동 근육 부위 테이블
    """
    __tablename__ = 'body'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    body_area = db.Column(db.String(48),nullable=False)

    exercise_set = db.relationship('Exercise', backref='body_set',cascade='all,delete')

    def __repr__(self):
        return f"Body : {self.id}"