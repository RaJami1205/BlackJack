"Proyecto 02 BlackJack // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.join(os.path.pardir, 'templates'), static_folder='static')
app.secret_key = 'ra&diegop'

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('interfaz_principal.html')

if __name__ == '__main__':
    app.run(debug=False)