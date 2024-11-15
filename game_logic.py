import random

baraja = [
    '2_of_spades', '3_of_spades', '4_of_spades', '5_of_spades', '6_of_spades', '7_of_spades', '8_of_spades', '9_of_spades', '10_of_spades', 'jack_of_spades', 'queen_of_spades', 'king_of_spades', 'ace_of_spades',  # Picas
    '2_of_hearts', '3_of_hearts', '4_of_hearts', '5_of_hearts', '6_of_hearts', '7_of_hearts', '8_of_hearts', '9_of_hearts', '10_of_hearts', 'jack_of_hearts', 'queen_of_hearts', 'king_of_hearts', 'ace_of_hearts',  # Corazones
    '2_of_diamonds', '3_of_diamonds', '4_of_diamonds', '5_of_diamonds', '6_of_diamonds', '7_of_diamonds', '8_of_diamonds', '9_of_diamonds', '10_of_diamonds', 'jack_of_diamonds', 'queen_of_diamonds', 'king_of_diamonds', 'ace_of_diamonds',  # Diamantes
    '2_of_clubs', '3_of_clubs', '4_of_clubs', '5_of_clubs', '6_of_clubs', '7_of_clubs', '8_of_clubs', '9_of_clubs', '10_of_clubs', 'jack_of_clubs', 'queen_of_clubs', 'king_of_clubs', 'ace_of_clubs',  # Tréboles
]

valores = {
    '2_of_spades': 2, '3_of_spades': 3, '4_of_spades': 4, '5_of_spades': 5, '6_of_spades': 6, '7_of_spades': 7, '8_of_spades': 8, '9_of_spades': 9, '10_of_spades': 10, 
    'jack_of_spades': 10, 'queen_of_spades': 10, 'king_of_spades': 10, 'ace_of_spades': 1, 
    '2_of_hearts': 2, '3_of_hearts': 3, '4_of_hearts': 4, '5_of_hearts': 5, '6_of_hearts': 6, '7_of_hearts': 7, '8_of_hearts': 8, '9_of_hearts': 9, '10_of_hearts': 10, 
    'jack_of_hearts': 10, 'queen_of_hearts': 10, 'king_of_hearts': 10, 'ace_of_hearts': 1, 
    '2_of_diamonds': 2, '3_of_diamonds': 3, '4_of_diamonds': 4, '5_of_diamonds': 5, '6_of_diamonds': 6, '7_of_diamonds': 7, '8_of_diamonds': 8, '9_of_diamonds': 9, '10_of_diamonds': 10, 
    'jack_of_diamonds': 10, 'queen_of_diamonds': 10, 'king_of_diamonds': 10, 'ace_of_diamonds': 1, 
    '2_of_clubs': 2, '3_of_clubs': 3, '4_of_clubs': 4, '5_of_clubs': 5, '6_of_clubs': 6, '7_of_clubs': 7, '8_of_clubs': 8, '9_of_clubs': 9, '10_of_clubs': 10, 
    'jack_of_clubs': 10, 'queen_of_clubs': 10, 'king_of_clubs': 10, 'ace_of_clubs': 1
}

def seleccionar_cartas():
    return random.sample(baraja, 2)

def seleccionar_carta():
    return random.choice(baraja)