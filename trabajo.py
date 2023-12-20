import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir el rango de valores para las variables difusas
x_soldados = np.arange(0, 31, 1)
x_nivel = np.arange(0, 101, 1)

# Definir funciones de membresía
soldados_pocos = fuzz.trapmf(x_soldados, [0, 0, 8, 12])
soldados_moderados = fuzz.trapmf(x_soldados, [5, 10, 15, 20])
soldados_muchos = fuzz.trapmf(x_soldados, [15, 20, 30, 30])

nivel_bajo = fuzz.trapmf(x_nivel, [0, 0, 25, 50])
nivel_medio = fuzz.trapmf(x_nivel, [25, 50, 50, 75])
nivel_alto = fuzz.trapmf(x_nivel, [50, 75, 100, 100])

# Visualización de funciones para soldados eliminados
plt.figure(figsize=(8, 4))
plt.plot(x_soldados, soldados_pocos, label='Pocos soldados')
plt.plot(x_soldados, soldados_moderados, label='Moderados soldados')
plt.plot(x_soldados, soldados_muchos, label='Muchos soldados')

plt.title('Funciones de membresía para cantidad de soldados eliminados')
plt.xlabel('Cantidad de soldados eliminados')
plt.ylabel('Pertenencia')
plt.legend()
plt.grid(True)
plt.show()

# Visualización de funciones de para nivel de habilidad
plt.figure(figsize=(8, 4))
plt.plot(x_nivel, nivel_bajo, label='Nivel Bajo')
plt.plot(x_nivel, nivel_medio, label='Nivel Medio')
plt.plot(x_nivel, nivel_alto, label='Nivel Alto')

plt.title('Funciones de membresía para nivel de habilidad')
plt.xlabel('Nivel de habilidad')
plt.ylabel('Pertenencia')
plt.legend()
plt.grid(True)
plt.show()
