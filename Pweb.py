from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '<a href="/sobre">Sobre Mim</a>' \
           '<br>' \
           '<a href="/experiencia">Experiencias</a>' \
           '<br>' \
           '<a href="/formacao">Formacao</a>' \
           '<br>' \
           '<a href="/contato">Contatos</a>' \

@app.route("/sobre", methods=["GET"])
def sobre():
    return 'Ola meu nomeé Wanderson Lucas. Sou estudante do IFCE Campus Cedro'

@app.route("/experiencia", methods=["GET"])
def experiencia():
    return 'Estágio supervisionado no provedor de internet Fast Net'

@app.route("/formacao", methods=["GET"])
def formacao():
    return 'Curso tecnico em Redes de COmputadores; <p>Bacharelando em Sistemas de Informação</p>'

@app.route("/contato", methods=["GET"])
def contato():
    return 'wanderson.lucas.loiola.06@aluno.ifce.edu.br'


if __name__ == "__main__":
    app.run(debug=True)