import math
import os

# Ecuación de Erlang C
def erlang_c(N, A):
    numerador = A ** N
    suma = sum((A ** k) / math.factorial(k) for k in range(N))
    denominador = numerador + math.factorial(N) * (1 - (A / N)) * suma
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
    return f"{round((numerador / math.factorial(N) * suma) / 10000, 6)}%"

def iter_variar_N(A, N_min, N_max, H, W0):
    for N in range(N_min, N_max + 1):
        C = erlang_c(N, A)
        B = erlang_b(N, A)
        W = tiempo_de_espera(N, A, H)
        P = probabilidad_espera(N, A, H, W0)
        if C is None:
            print(f"{N:>4} {'—':>10} {B:>10.4f} {'—':>10} {'—':>10}")
        else:
            print(f"{N:>4} {C:>10.4f} {B:>10.4f} {W:>10.2f} {P:>10.4f}")



"""
Hacer un servidor que genere tráfico TCP, bajado de http/https
Probar el servidor de Redes 1
"""


# Call center tiene número de lineas/troncales y agentes
# Para determinar número de lineas, es necesario alquilarlas primero, sino es una estimación
# H = 120 s
# W0 = 30 s
# N = 8 agentes (>A)
# A = (pico-llamadas/hora-pico * promedio llamada)/3600 = (180 llamadas/hora * 120 s)/3600 = 6 erlangs o más en base al estimado
H = 120
W0 = 30
N = 9
A = 7.2

print(erlang_c(N, A))
print(tiempo_de_espera(H, N, A))
print(probabilidad_espera(W0, N, A, H))

# R1.1: Con mínimo 8 agentes se cumple el QoS
# R1.2: Es necesario rediseñar el sistema, ya qu ela espera se convierte en 105 s, superior a los 30s esperados
# Para mantener el QoS deseado (P(W>30s)), es necesario tener 9 agentes

A = (((190+193)/2)*140)/3600
# A = 7.45 E
# N = 8
N = 18
H = 140
W0 = 20
print("")
print(erlang_c(N, A))
print(tiempo_de_espera(H, N, A))
print(probabilidad_espera(W0, N, A, H))
print(erlang_b(N, A))