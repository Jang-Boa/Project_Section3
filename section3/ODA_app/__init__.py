from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy() # 전역 변수로 db 객체 생성
migrate = Migrate() # 전역 변수로 migrate 객체 생성

def create_app(config=None):
    app = Flask(__name__)

    # db connect
    app.config.from_object(config) # config.py 파일에 작성한 항목을 환경변수로 부르기 위해 작성
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exercise.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# ORM
    with app.app_context(): # db 와 migrate 객체 초기화 
        db.init_app(app)
        migrate.init_app(app,db)

    from . import models

    # blueprint -> route
    from ODA_app.routes import main_route, exercise_route, community_route
    app.register_blueprint(main_route.bp)
    app.register_blueprint(exercise_route.bp)#,url_prefix='/exercise')
    app.register_blueprint(community_route.bp)


    return app

if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)