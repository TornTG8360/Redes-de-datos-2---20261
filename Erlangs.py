import math

# Ecuación de Erlang C
def erlang_c(N, A):
    numerador = A ** N
    suma = sum((A ** k) / math.factorial(k) for k in range(N))
    denominador = numerador + math.factorial(n) * (1 - (A / N)) * suma
    return numerador / denominador

# Ecuación de W
def tiempo_de_espera(H, N, A):
    c = erlang_c(N, A)
    return c * H / (N - A)

# Probabilidad en QoS de espera
def probabilidad_espera(W0, N, A, H):
    c = erlang_c(N, A)
    return c * math.exp(- (N - A) * W0 / H)

# Erlang B para probabilidad en QoS de bloqueo
def erlang_b(N, A):
    numerador = A ** N 
    suma = sum((A**k) / math.factorial(k) for k in range(N + 1))
    return numerador / math.factorial(N) * suma

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

