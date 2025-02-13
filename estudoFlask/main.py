from flask import Flask, redirect, url_for, request, abort, render_template, make_response, session
from json import dumps
import json


app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "chaveSecreta"

# criando a rota de outr maneira

def teste():
    return "<h1>Olá (teste)</h1>"

app.add_url_rule("/teste", "teste", teste)

# ROTAS DINÂMICAS
@app.route("/hello/")
@app.route("/hello/<nome>")
def hello(nome=""):
    return "<h1>Olá {}</h1>".format(nome)

@app.route("/hello2/")
@app.route("/hello2/<int:id>")
def hello2(id = -1):
    if id >= 0:
        return "Opan {}".format(id)
    else:
        return "OPAN NO ELSE"


# Construção de URL
@app.route("/admin")
def admin():
    return "<h1>admin</h1>"

@app.route("/guest/<guest>")
def guest(guest):
    return "<h1>Olá guest <b>%s</b></h1>" % guest

@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("guest", guest = name))


# Arquivos estáticos / metódos http
@app.route("/add", methods=["GET","POST"])
def add():
    # para pegar os dados tem dois jeitos
    if request.method == "POST":
        # esse:
        # return "Opan POST result: %s" % request.form['nome']
        # e esse que retorna um JSON:
        return dumps(request.form)
    return "Opan GET result: %s" % request.form['nome']


# Objetos de requisição
@app.route("/", methods=["GET","POST"])
def index2():
    print(request.method,request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t1,t2])


# Redirecionamento e erros
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form['username'] == "admin" and request.form['pass'] == "admin":
            return redirect(url_for("sucesso"), code=302)
        else:
            abort(401)
    else:
        abort(403) # serve para mostrar o status caso der erro

@app.route("/sucesso")
def sucesso():
    return "SUCESSO NO LOGIN"


# Cookies
@app.route("/cookie")
def cookie():
    return render_template("cookies.html")


@app.route("/setCookies", methods=['GET','POST'])
def setCookies():

    resp = make_response(render_template('setCookie.html'))
    
    if request.method == "POST":
        dados = request.form['c']
        resp.set_cookie('testeCookies', dados)

    return resp

@app.route("/getCookies")
def getCookies():
    cookieName = request.cookies.get('testeCookies')
    return '<h1>O valor do Cookie é: {}</h1>'.format(cookieName)


@app.route("/session")
def session_page():  # Nome diferente para evitar conflito
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('session.html', username=username)

@app.route("/login2", methods=['GET', 'POST'])
def login2():
    if request.method == "POST":
        session['username'] = request.form['username'] 
        return redirect(url_for('session_page')) 
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('session_page'))





if __name__ == "__main__":
    app.run(debug=True) # aqui caso eu queria mudar a porta do servidor só colocar port=3000 ou selá lá qual for.