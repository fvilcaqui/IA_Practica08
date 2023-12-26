import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir rango de valores para las variables difusas
x_soldados = np.arange(0, 31, 1)
x_nivel = np.arange(0, 101, 1)
x_vidas = np.arange(0, 101, 1)
x_tiempo = np.arange(0, 61, 1)  # Corregido el rango de valores para el tiempo

# Definir funciones de membresía para soldados eliminados
soldados_pocos = fuzz.trapmf(x_soldados, [0, 0, 8, 12])
soldados_moderados = fuzz.trapmf(x_soldados, [5, 10, 15, 20])
soldados_muchos = fuzz.trapmf(x_soldados, [15, 20, 30, 30])

# Definir funciones de membresía para nivel de habilidad
nivel_bajo = fuzz.trapmf(x_nivel, [0, 0, 25, 50])
nivel_medio = fuzz.trapmf(x_nivel, [25, 50, 50, 75])
nivel_alto = fuzz.trapmf(x_nivel, [50, 75, 100, 100])

# Definir funciones de membresía para cantidad de vidas perdidas
vida_poca = fuzz.trapmf(x_vidas, [0, 0, 33, 40])
vida_moderada = fuzz.trapmf(x_vidas, [25, 38, 66, 78])
vida_bastante = fuzz.trapmf(x_vidas, [60, 70, 100, 100])  # Corregido el rango

# Definir funciones de membresía para tiempo utilizado para pasar de nivel
tiempo_bajo = fuzz.trapmf(x_tiempo, [0, 0, 20, 25])
tiempo_medio = fuzz.trapmf(x_tiempo, [15, 23, 35, 45])
tiempo_alto = fuzz.trapmf(x_tiempo, [35, 42, 60, 60])

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

# Visualización de funciones para nivel de habilidad
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

# Visualización de funciones para cantidad de vidas perdidas
plt.figure(figsize=(8, 4))
plt.plot(x_vidas, vida_poca, label='Vida Poca')
plt.plot(x_vidas, vida_moderada, label='Vida Moderada')
plt.plot(x_vidas, vida_bastante, label='Vida Bastante')

plt.title('Funciones de membresía para cantidad de vidas perdidas')
plt.xlabel('Cantidad de vidas perdidas')
plt.ylabel('Pertenencia')
plt.legend()
plt.grid(True)
plt.show()

# Visualización de funciones para tiempo utilizado para pasar de nivel
plt.figure(figsize=(8, 4))
plt.plot(x_tiempo, tiempo_bajo, label='Poco Tiempo')
plt.plot(x_tiempo, tiempo_medio, label='Moderado Tiempo')
plt.plot(x_tiempo, tiempo_alto, label='Mucho Tiempo')

plt.title('Funciones de membresía para tiempo utilizado para pasar de nivel')
plt.xlabel('Tiempo utilizado')
plt.ylabel('Pertenencia')
plt.legend()
plt.grid(True)
plt.show()

nivel_actual = nivel_medio
# Valores específicos para evaluar (ejemplo de valores)
valor_soldados = 10
valor_vidas = 40
valor_tiempo = 30

# Calcular la pertenencia de los valores específicos a cada función de membresía
pert_soldados_pocos = fuzz.interp_membership(x_soldados, soldados_pocos, valor_soldados)
pert_soldados_moderados = fuzz.interp_membership(x_soldados, soldados_moderados, valor_soldados)
pert_soldados_muchos = fuzz.interp_membership(x_soldados, soldados_muchos, valor_soldados)

pert_vida_poca = fuzz.interp_membership(x_vidas, vida_poca, valor_vidas)
pert_vida_moderada = fuzz.interp_membership(x_vidas, vida_moderada, valor_vidas)
pert_vida_bastante = fuzz.interp_membership(x_vidas, vida_bastante, valor_vidas)

pert_tiempo_bajo = fuzz.interp_membership(x_tiempo, tiempo_bajo, valor_tiempo)
pert_tiempo_medio = fuzz.interp_membership(x_tiempo, tiempo_medio, valor_tiempo)
pert_tiempo_alto = fuzz.interp_membership(x_tiempo, tiempo_alto, valor_tiempo)

# Condiciones difusas para nivel_bajo y nivel_medio
cond_nivel_bajo = (
    (pert_soldados_pocos and pert_vida_poca and pert_tiempo_alto) or
    (pert_soldados_pocos and pert_vida_poca and pert_tiempo_medio) or
    (pert_soldados_moderados and pert_vida_poca and pert_tiempo_medio) or
    (pert_soldados_pocos and pert_vida_moderada and pert_tiempo_medio)
)

cond_nivel_medio = (
    (pert_soldados_pocos and pert_vida_poca and pert_tiempo_bajo) or
    (pert_soldados_muchos and pert_vida_poca and pert_tiempo_alto) or
    (pert_soldados_pocos and pert_vida_bastante and pert_tiempo_alto) or
    (pert_soldados_moderados and pert_vida_moderada and pert_tiempo_medio) or
    (pert_soldados_moderados and pert_vida_moderada and pert_tiempo_alto) or
    (pert_soldados_pocos and pert_vida_moderada and pert_tiempo_medio) or
    (pert_soldados_moderados and pert_vida_poca and pert_tiempo_medio) or
    (pert_soldados_moderados and pert_vida_moderada and pert_tiempo_bastante)
)

if cond_nivel_bajo:
    nivel_actual = nivel_bajo
    print("El nivel ha cambiado a: Nivel Bajo")
elif cond_nivel_medio:
    nivel_actual = nivel_medio
    print("El nivel sigue siendo: Nivel Medio")
else:
    nivel_actual = nivel_alto
    print("El nivel ha cambiado a: Nivel Alto")