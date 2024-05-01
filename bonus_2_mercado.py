from pulp import *

# Crear un problema de minimización
prob = LpProblem("Compra de contenedores", LpMinimize)

# Variables de decisión
x = LpVariable("Contenedores_Raul", lowBound=0, cat='Integer')  
y = LpVariable("Contenedores_Javier", lowBound=0, cat='Integer')  

# Función objetivo: minimizar la distancia total
prob += 150 * x + 300 * y

# Restricciones: cantidad de frutas requeridas
prob += 8 * x + 2 * y >= 16  
prob += 1 * x + 1 * y >= 5   
prob += 2 * x + 7 * y >= 20  

# Resolver el problema
prob.solve()

# Imprimir resultados
print("Cantidad de contenedores comprados a Raúl:", value(x))
print("Cantidad de contenedores comprados a Javier:", value(y))
print("Distancia total recorrida:", value(prob.objective))