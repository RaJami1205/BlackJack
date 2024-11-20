"Proyecto 02 BlackJack // Curso de Análisis de Algoritmos // Diego y Raúl"
"Código main"

from flask import Flask, render_template, redirect, url_for
from game_logic import seleccionar_cartas, seleccionar_carta, inicializar_baraja, valores

app = Flask(__name__)
app.secret_key = 'ra&diegop'

# Variables globales para la baraja, las cartas de los jugadores, el resultado del conteo
# y la lista de los ganadores
baraja_disponible = None
cartas_crupier = None
cartas_jugador = None
cartas_IA1 = None
cartas_IA2 = None
lista_ganadores = None

@app.route('/')
def index():
    return render_template('interfaz_principal.html')

@app.route('/comenzar_partida', methods=['POST'])
def comenzar_partida():
    global baraja_disponible, cartas_crupier, cartas_jugador, cartas_IA1, cartas_IA2, lista_ganadores
    resultado_jugador = 0
    resultado_IA1 = 0
    resultado_IA2 = 0
    lista_ganadores = []

    # Inicializa la baraja y reparte las cartas
    baraja_disponible = inicializar_baraja()
    cartas_crupier = seleccionar_cartas(baraja_disponible, 2)
    cartas_jugador = seleccionar_cartas(baraja_disponible, 2)
    cartas_IA1 = seleccionar_cartas(baraja_disponible, 2)
    cartas_IA2 = seleccionar_cartas(baraja_disponible, 2)
    
    # Ciclo para el conteo de las cartas
    for carta in cartas_jugador:
        resultado_jugador += valores.get(carta)

    for carta in cartas_IA1:
        resultado_IA1 += valores.get(carta)

    for carta in cartas_IA2:
        resultado_IA2 += valores.get(carta)
    
    # Verifica si el jugador ganó o perdió al inicio
    if resultado_jugador == 21:
        lista_ganadores.append("Tú")
    
    if resultado_IA1 == 21:
        lista_ganadores.append("IA_1")
    
    if resultado_IA2 == 21:
        lista_ganadores.append("IA_2")

    if len(lista_ganadores) == 1:
        return render_template('interfaz_ganador.html', player=lista_ganadores[0])
    elif len(lista_ganadores) > 1:
        return render_template('interfaz_empate.html', lista_ganadores=lista_ganadores)

    # Pasa las cartas al template principal
    carta_crupier_svg = url_for('static', filename=f'SVG-cards-1.3/{cartas_crupier[0]}.svg')

    return render_template(
    'interfaz_principal.html',
    cartas_player=cartas_jugador,
    cartas_IA_player1=cartas_IA1,
    cartas_IA_player2=cartas_IA2,
    carta_crupier=carta_crupier_svg,
    resultado_jugador=resultado_jugador,
    resultado_IA1=resultado_IA1,
    resultado_IA2=resultado_IA2
)

# Ruta para pedir una carta (Seguir)
@app.route('/pedir_carta', methods=['POST'])
def pedir_carta():
    global baraja_disponible, cartas_crupier, cartas_jugador, cartas_IA1, cartas_IA2
    resultado_crupier = 0
    resultado_jugador = 0
    resultado_IA1 = 0
    resultado_IA2 = 0

    # El jugador principal pide una carta
    cartas_jugador.append(seleccionar_carta(baraja_disponible))

    # Conteo de cartas
    for carta in cartas_crupier:
        resultado_crupier += valores.get(carta)
    for carta in cartas_jugador:
        resultado_jugador += valores.get(carta)
    for carta in cartas_IA1:
        resultado_IA1 += valores.get(carta)
    for carta in cartas_IA2:
        resultado_IA2 += valores.get(carta)

    if resultado_jugador == 21:
        return render_template('interfaz_ganador.html', player='Tú')

    if resultado_jugador > 21:
        ganadores = []

        ia_data = [
            ("IA_1", cartas_IA1, resultado_IA1),
            ("IA_2", cartas_IA2, resultado_IA2),
        ]

        for nombre_ia, cartas_ia, resultado_ia in ia_data:
            while resultado_ia < 21:
                cartas_ia.append(seleccionar_carta(baraja_disponible))
                resultado_ia = sum(valores.get(carta) for carta in cartas_ia)
                if resultado_ia > 21:
                    break  

            if resultado_ia == 21:
                return render_template('interfaz_ganador.html', player='IA')

        while resultado_crupier < 17:
            cartas_crupier.append(seleccionar_carta(baraja_disponible))
            resultado_crupier = sum(valores.get(carta) for carta in cartas_crupier)

        if resultado_crupier == 21:
            return render_template('interfaz_ganador.html', player='Casa')

        if not ganadores:
            puntajes = [
                ("Casa", resultado_crupier if resultado_crupier <= 21 else 0),
                ("IA_1", resultado_IA1 if resultado_IA1 <= 21 else 0),
                ("IA_2", resultado_IA2 if resultado_IA2 <= 21 else 0),
            ]
            
            ganador_cercano = max(puntajes, key=lambda x: x[1])

            ganadores = [nombre for nombre, puntaje in puntajes if puntaje == ganador_cercano[1]]

        if len(ganadores) == 1:
            return render_template('interfaz_ganador.html', player=ganadores[0])

        return render_template('interfaz_empate.html', lista_ganadores=ganadores)

    return render_template(
        'interfaz_principal.html',
        cartas_player=cartas_jugador,
        cartas_IA_player1=cartas_IA1,
        cartas_IA_player2=cartas_IA2,
        carta_crupier=cartas_crupier[0],
        resultado_crupier=resultado_crupier,
        resultado_jugador=resultado_jugador,
        resultado_IA1=resultado_IA1,
        resultado_IA2=resultado_IA2
    )

# Ruta para retirarse (Parar)
@app.route('/retirarse', methods=['POST'])
def retirarse():
    global baraja_disponible, cartas_crupier, cartas_IA1, cartas_IA2
    resultado_crupier = 0
    resultado_IA1 = 0
    resultado_IA2 = 0

    # Recalcular resultados iniciales
    for carta in cartas_crupier:
        resultado_crupier += valores.get(carta)
    for carta in cartas_IA1:
        resultado_IA1 += valores.get(carta)
    for carta in cartas_IA2:
        resultado_IA2 += valores.get(carta)

    ganadores = []

    ia_data = [
        ("IA_1", cartas_IA1, resultado_IA1),
        ("IA_2", cartas_IA2, resultado_IA2),
    ]

    for nombre_ia, cartas_ia, resultado_ia in ia_data:
        while resultado_ia < 21:
            cartas_ia.append(seleccionar_carta(baraja_disponible))
            resultado_ia = sum(valores.get(carta) for carta in cartas_ia)
            if resultado_ia > 21:
                break 

        if resultado_ia == 21:
            return render_template('interfaz_ganador.html', player='IA')

    while resultado_crupier < 17:
        cartas_crupier.append(seleccionar_carta(baraja_disponible))
        resultado_crupier = sum(valores.get(carta) for carta in cartas_crupier)

    if resultado_crupier == 21:
        return render_template('interfaz_ganador.html', player='Casa')

    if not ganadores:
        puntajes = [
            ("Casa", resultado_crupier if resultado_crupier <= 21 else 0),
            ("IA_1", resultado_IA1 if resultado_IA1 <= 21 else 0),
            ("IA_2", resultado_IA2 if resultado_IA2 <= 21 else 0),
        ]
    
        ganador_cercano = max(puntajes, key=lambda x: x[1])

        ganadores = [nombre for nombre, puntaje in puntajes if puntaje == ganador_cercano[1]]

    if len(ganadores) == 1:
        return render_template('interfaz_ganador.html', player=ganadores[0])

    return render_template('interfaz_empate.html', lista_ganadores=ganadores)


if __name__ == '__main__':
    app.run(debug=True)