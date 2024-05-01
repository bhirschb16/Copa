import numpy as np

def mezclar_baraja():
    baraja = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    np.random.shuffle(baraja)  
    return ''.join(baraja)  

def contiene_dos_reyes_seguidos(baraja):
    return 'KK' in baraja

# Simulación de Montecarlo
num_simulaciones = 100000
num_veces_dos_reyes_seguidos = sum(contiene_dos_reyes_seguidos(mezclar_baraja()) for _ in range(num_simulaciones))

# Calcular la probabilidad
probabilidad = num_veces_dos_reyes_seguidos / num_simulaciones

print("La probabilidad de encontrar dos reyes seguidos en una baraja mezclada aleatoriamente es:", probabilidad)