from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "My index"

# criando a rota de outr maneira

def teste():
    return "<h1>Olá (teste)</h1>"

app.add_url_rule("/teste", "teste", teste)

if __name__ == "__main__":
    app.run(debug=True)