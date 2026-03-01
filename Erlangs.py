import math
import os

# Ecuación de Erlang C
def erlang_c(N, A):
    numerador = A ** N
    suma = sum((A ** k) / math.factorial(k) for k in range(N))
    denominador = numerador + math.factorial(N) * (1 - (A / N)) * suma
    print(numerador, denominador)
    return round(numerador / denominador, 6)

# Ecuación de W
def tiempo_de_espera(H, N, A):
    c = erlang_c(N, A)
    return round(c * H / (N - A), 6)

# Probabilidad en QoS de espera
def probabilidad_espera(W0, N, A, H):
    c = erlang_c(N, A)
    return f"{round((c * math.exp(- (N - A) * W0 / H)) * 100, 6)}%"

# Erlang B para probabilidad en QoS de bloqueo
def erlang_b(N, A):
    numerador = A ** N
    suma = sum((A**k) / math.factorial(k) for k in range(N + 1))
    denominador = math.factorial(N) * suma
    print(numerador, denominador)
    return f"{round((numerador / denominador) * 100, 6)}%"

# Call center tiene número de lineas/troncales y agentes
# Para determinar número de lineas, es necesario alquilarlas primero, sino es una estimación
os.system("clear")
A = 7.5056
N = 12
print(N-A)
H = 140
W0 = 20
print("Punto 2")
print(f"Erlang B - Posibilidad de Bloqueo: {erlang_b(N, A)}")
print(f"Erlang C: {erlang_c(N, A)}")
print(f"Tiempo de espera: {tiempo_de_espera(H, N, A)}")
print(f"Posibilidad de esperar más de {W0} segundos: {probabilidad_espera(W0, N, A, H)}")


