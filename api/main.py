import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Se você abrir o chrome e acessar o site localhost:5000/index ou 127.0.0.1 é exibido a tag html abaixo
# <h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>

@app.route('/index', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# Dados para teste
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

# Essa "rota" retorna todos os nossos dados !
# Basta acessa-la pelo navegador em 127.0.0.1:5000/api/v1/resources/books/all ou localhost:5000/api/v1/resources/books/all
# Você pode chamar rotas usando o POSTMAN !
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return books


app.run()