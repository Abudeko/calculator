# Importações
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variáveis usadas para o cálculo do consumo dos aparelhos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef


# Primeira página
@app.route('/')
def index():
    return render_template('index.html')


# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
        'lights.html',
        size=size
    )


# Terceira página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
        'electronics.html',
        size=size,
        lights=lights
    )


# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template(
        'end.html',
        result=result_calculate(
            int(size),
            int(lights),
            int(device)
        )
    )


# O formulário
@app.route('/form')
def form():
    return render_template('form.html')


# Resultados do formulário
@app.route('/submit', methods=['POST'])
def submit_form():
    # Coletar dados do formulário
    nome = request.form['name']
    email = request.form['email']
    endereco = request.form['address']
    data = request.form['date']

    # Salvar os dados no arquivo form.txt
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f'Nome: {nome}\n')
        f.write(f'Email: {email}\n')
        f.write(f'Endereço: {endereco}\n')
        f.write(f'Data: {data}\n')
        f.write('------------------------\n')

    # Exibir os dados na página de resultado
    return render_template(
        'form_result.html',
        name=nome,
        email=email,
        address=endereco,
        date=data
    )


app.run(debug=True)
