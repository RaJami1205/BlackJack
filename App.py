"Proyecto 02 BlackJack // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, redirect, url_for
from game_logic import seleccionar_cartas, seleccionar_carta, inicializar_baraja, valores

app = Flask(__name__)
app.secret_key = 'ra&diegop'

# Variables globales para la baraja y las cartas de los jugadores
baraja_disponible = inicializar_baraja()
cartas_crupier = None
cartas_jugador = None
cartas_IA1 = None
cartas_IA2 = None

@app.route('/')
def index():
    return render_template('interfaz_principal.html')

@app.route('/comenzar_partida', methods=['POST'])
def comenzar_partida():
    global baraja_disponible, cartas_jugador, cartas_IA1, cartas_IA2
    resultado_crupier = 0
    resultado_jugador = 0
    resultado_IA1 = 0
    resultado_IA2 = 0

    # Inicializa la baraja y reparte las cartas
    baraja_disponible = inicializar_baraja()
    cartas_crupier = seleccionar_cartas(baraja_disponible, 2)
    cartas_jugador = seleccionar_cartas(baraja_disponible, 2)
    cartas_IA1 = seleccionar_cartas(baraja_disponible, 2)
    cartas_IA2 = seleccionar_cartas(baraja_disponible, 2)

    for carta in cartas_crupier:
        resultado_crupier += valores.get(carta)
    
    for carta in cartas_jugador:
        resultado_jugador += valores.get(carta)

    for carta in cartas_IA1:
        resultado_IA1 += valores.get(carta)

    for carta in cartas_IA2:
        resultado_IA2 += valores.get(carta)

    # Pasa las cartas al template
    return render_template(
        'interfaz_principal.html',
        cartas_player=cartas_jugador,
        cartas_IA_player1=cartas_IA1,
        cartas_IA_player2=cartas_IA2,
        resultado_jugador=resultado_jugador,
        resultado_IA1=resultado_IA1,
        resultado_IA2=resultado_IA2
    )

# Ruta para pedir una carta (Seguir)
@app.route('/pedir_carta', methods=['POST'])
def pedir_carta():
    global baraja_disponible, cartas_jugador, cartas_IA1, cartas_IA2
    resultado_jugador = 0
    resultado_IA1 = 0
    resultado_IA2 = 0

    cartas_jugador.append(seleccionar_carta(baraja_disponible))

    for carta in cartas_jugador:
        resultado_jugador += valores.get(carta)

    for carta in cartas_IA1:
        resultado_IA1 += valores.get(carta)

    for carta in cartas_IA2:
        resultado_IA2 += valores.get(carta)

    
    # Redirigir de nuevo a la página principal después de pedir carta
    return render_template(
        'interfaz_principal.html',
        cartas_player=cartas_jugador,
        cartas_IA_player1=cartas_IA1,
        cartas_IA_player2=cartas_IA2,
        resultado_jugador=resultado_jugador,
        resultado_IA1=resultado_IA1,
        resultado_IA2=resultado_IA2
    )

# Ruta para retirarse (Parar)
@app.route('/retirarse', methods=['POST'])
def retirarse():
    # Aquí puedes agregar la lógica para finalizar la partida
    print("El jugador se ha retirado.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)