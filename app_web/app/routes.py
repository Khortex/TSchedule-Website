from app import app 
from flask import Blueprint, Flask, render_template, flash, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, FlaskForm, CadastroForm, PostagemForm
from app import db, forms
from .models import  Posts, User
import sqlite3
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
routes = Blueprint('routes', __name__)

con = sqlite3.connect("db.db")
login_manager = LoginManager() 
login_manager.init_app(app) 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home', user=User)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        nome=form.username.data
        user=User.query.filter_by(username=nome).first()
        
        if user and user.password == form.password.data:
            login_user(user, remember = form.remember_me.data)
            return render_template("materias.html")
        else:
            flash("Login Inválido")

    return render_template("login.html", title = "Login", form=form,)
    
@app.route("/materias", methods = ["POST", "GET"])
@login_required
def materias():
    if request.method  == "POST":
        materia = request.form["Disciplina"]
        return render_template('materias.html', title= 'Matérias', materia = materia)

    return render_template('materias.html', title= 'Matérias')


@app.route("/sobre", methods = ["POST", "GET"])
def sobre():
    if request.method  == "POST":
        return render_template('materias.html', title= 'Sobre Nós', sobre = sobre)
    return render_template('sobre.html', title= 'Sobre Nós')

@app.route('/cadastro', methods=["POST", "GET"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        name=form.username.data
        senha=form.password.data
        user=User(username=name,password=senha)
        db.session.add(user)
        db.session.commit()
        flash("Registro Feito com Sucesso")
        redirect(url_for("index"))
    return render_template("cadastro.html", title = "Cadastro", form=form,)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/postagens", methods = ["POST", "GET"])
@login_required
def postagens():
    form = PostagemForm()
    Chat = Posts.query.order_by(Posts.id).first()
    if form.validate_on_submit():
        user_id = current_user.username
        body = form.body.data
        imagem = form.imagem.object_data
        Post = Posts(user_id = user_id, body = body, imagem = imagem)
        db.session.add(Post)
        db.session.commit()
        chat = Posts.query.all()
        print(chat)
        flash("Postagem Realizada!")
        
    return render_template('postagens.html', title= 'T-ScheduleChat', Chat = Chat, form = form)
    
'''
q = "SELECT user_id, body, imagem FROM Posts"
    my_c=con.execute(q)
    Post=my_c.fetchone()
    print("Usuario:", Post [3])
    print("id", Post [0], "\n")
    print("body", Post [1],"\n")
    print("imagem", Post [4],"\n")    
'''   
