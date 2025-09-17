from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# ---configuração do banco de dados ---

#define uma chave chave secreta para aplicação. É necessário para o flash
#em produção, use uma chave mais complexa e segura
app.secret_key = 'minha_chave_secreta'

#configura a URL do banco de dados. O SQLite é um banco de dados de arquivo único
#o arquivo 'site.db' será cirado automaticamente na pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#cria as instâncias do SQLAlchemy e Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# --- Definição do Modelo de Dados ---

# a classe 'User' representa a tabela de usuários no banco de dados
class User(db.Model):
    # 'db.Column' define uma coluna na tabela
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    #método de representação para facilitar a visualização em logs
    def __repr__(self):
        return f"User('{self.email}')"

@app.route('/login', methods=['GET', 'POST'])
def login():
    #se o método da requisição for POST, o formulário foi enviado
    if request.method == 'POST':
        #request.form é um dicionário com os dados do formulário
        email = request.form['email']
        password = request.form['password']

        flash('Lógica de login ainda não implementa.', 'info')
        #por enquanto, apenas exibe os dados para confirmar que estão sendo recebidos
        return render_template(url_for(login))
    
    #se o método for GET, simplesmente redereiza o template
    return render_template('login.html')

#rota para a página de cadastro
#também aceita os métodos GET, POST
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.form == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        #aqui vamos adicionar a lógica de validação e salvamentona próxima etapa
        #por enquanto, apenas redireciona para a página de cadastro
        flash('Lógica de cadastro ainda não implementada.','info')
        return render_template('register')
    
    return render_template('register.html')

# --- execução da aplicação ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        app.run(debug=True)