from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pega os dados do formulário
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('msg')
        
        # Salva os dados em um arquivo texto
        with open('data.txt', 'a') as file:
            file.write(f'Name: {name}, Email: {email}, Mesage: {msg}\n')
        
        # Redireciona para a página de confirmação
        return redirect(url_for('confirmation'))
    
    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/data')
def data():
    # Lê os dados do arquivo
    try:
        with open('data.txt', 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        content = []
    
    # Envia as linhas com índices
    data = [(index, line) for index, line in enumerate(content)]
    
    return render_template('data.html', data=data)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    # Lê os dados do arquivo
    try:
        with open('data.txt', 'r') as file:
            lines = file.readlines()
        
        # Remove a linha desejada
        if 0 <= index < len(lines):
            lines.pop(index)
        
        # Reescreve o arquivo sem a linha excluída
        with open('data.txt', 'w') as file:
            file.writelines(lines)
    
    except FileNotFoundError:
        pass
    
    return redirect(url_for('data'))
if __name__ == '__main__':
    app.run(debug=True)
