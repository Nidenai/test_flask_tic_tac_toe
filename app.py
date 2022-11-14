from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
api = Api(app)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamename = db.Column(db.String(80), nullable=False)
    gamedata = db.Column(db.Text(120))
    gameturn = db.Column(db.Integer)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


class Main(Resource):
    def get(self):
        return User.query.all()


api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True)
