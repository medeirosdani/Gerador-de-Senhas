# Importa o Flask e funções úteis:
# - Flask: cria o servidor
# - render_template: carrega arquivos HTML
# - request: pega dados enviados pelo formulário
from flask import Flask, render_template, request

# Biblioteca para gerar caracteres aleatórios
import random
import string

# Cria o aplicativo Flask (obrigatório em todo projeto Flask)
app = Flask(__name__)


# Função que realmente gera a senha
def gerar_senha(tamanho):
    # Conjunto de caracteres permitidos (letras + números)
    caracteres = string.ascii_letters + string.digits

    # Gera a senha escolhendo 'tamanho' caracteres aleatórios
    # ''.join(...) junta tudo em uma única string
    return ''.join(random.choice(caracteres) for _ in range(tamanho))


# Rota principal do site (URL "/")
# methods define quais métodos HTTP ela aceita (GET = abrir, POST = enviar formulário)
@app.route('/', methods=['GET', 'POST'])
def index():

    senha = None  # Começa sem senha gerada

    # Se o usuário clicou no botão "Gerar" → método será POST
    if request.method == 'POST':

        # Pega o número enviado pelo formulário HTML
        tamanho = int(request.form['tamanho'])

        # Gera a senha com o tamanho informado
        senha = gerar_senha(tamanho)

    # Envia o valor para o HTML (mesmo que seja None)
    return render_template('index.html', senha=senha)


# Executa o servidor Flask se o arquivo for rodado diretamente
if __name__ == "__main__":

    # debug=True permite ver erros e recarregar o servidor automaticamente
    app.run(debug=True)