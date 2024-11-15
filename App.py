"Proyecto 02 BlackJack // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, redirect, url_for, session
from game_logic import seleccionar_cartas, seleccionar_carta  # Asumiendo que tienes esta función

app = Flask(__name__)
app.secret_key = 'ra&diegop'

cartas_jugador = None

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('interfaz_principal.html')

# Ruta para comenzar la partida
@app.route('/comenzar_partida', methods=['POST'])
def comenzar_partida():
    global cartas_jugador
    # Seleccionar cartas para el jugador
    cartas_jugador = seleccionar_cartas()
    
    # Redirigir de nuevo a la página principal después de comenzar la partida
    return render_template('interfaz_principal.html', cartas=cartas_jugador)

# Ruta para pedir una carta (Seguir)
@app.route('/pedir_carta', methods=['POST'])
def pedir_carta():
    global cartas_jugador
    carta = seleccionar_carta()

    if carta in cartas_jugador:
        pedir_carta()

    cartas_jugador.append(carta)
    print("Cartas del jugador (después de pedir carta):", cartas_jugador)
    
    # Redirigir de nuevo a la página principal después de pedir carta
    return render_template('interfaz_principal.html', cartas=cartas_jugador)

# Ruta para retirarse (Parar)
@app.route('/retirarse', methods=['POST'])
def retirarse():
    # Aquí puedes agregar la lógica para finalizar la partida
    print("El jugador se ha retirado.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)