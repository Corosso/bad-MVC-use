from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Aquí iría la lógica para procesar el formulario correcto
    return redirect(url_for('bad_form'))  # Redirigir a la vista incorrecta

@app.route('/bad_form')
def bad_form():
    return render_template('bad_form.html')

if __name__ == '__main__':
    app.run(debug=True)
