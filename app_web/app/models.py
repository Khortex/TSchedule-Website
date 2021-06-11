from sqlalchemy.orm import backref
from app import db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#tabela de usuários

class User(UserMixin, db.Model):
    __tablename__= 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique = True)
    password = db.Column(db.String(120))
    Posts = db.relationship("Posts", backref="author", lazy="dynamic")
    def __repr__(self):
        return "<User {}>".format(self.username)

#tabela de posts
class Posts(db.Model):
    __tablename__= 'Posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.username'))
    body = db.Column(db.String(140))
    imagem = db.Column(db.BLOB)
    #comentario_id = db.Column(db.Integer, db.ForeignKey('comentario.id'))
    #comentario = db.relationship("Posts", backref = backref("Posts"), lazy="dynamic")
    #parent_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    #timestamp = db.Column(db.Integer, index=True)
    def __repr__(self):
        return '<Posts {}>'.format(self.body)

db.create_all()
db.session.commit()
