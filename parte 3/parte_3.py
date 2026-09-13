
import random
import matplotlib.pyplot as plt

def calcular_error_relativo(teorico, numerico):
    if teorico == 0:
        return float('inf')  # Evitar división por cero
    return abs((teorico - numerico) / teorico)

def suma_mayor_a_menor(N):
    resultado_teorico = N/(N+1)
    resultado_numerico = 0
    for k in range(N, 0, -1):
        termino_k = 1/(k*(k+1))
        resultado_numerico += termino_k
    error_relativo = calcular_error_relativo(resultado_teorico, resultado_numerico)
    return resultado_teorico, resultado_numerico, error_relativo

def suma_menor_a_mayor(N):
    resultado_teorico = N/(N+1)
    resultado_numerico = 0
    for k in range(1, N+1):
        termino_k = 1/(k*(k+1))
        resultado_numerico += termino_k
    error_relativo = calcular_error_relativo(resultado_teorico, resultado_numerico)
    return resultado_teorico, resultado_numerico, error_relativo

def suma_orden_aleatorio(N):
    resultado_teorico = N/(N+1)
    resultado_numerico = 0
    orden_aleatorio = random.sample(range(1, N+1), N)

    for k in orden_aleatorio:
        termino_k = 1/(k*(k+1))
        resultado_numerico += termino_k

    error_relativo = calcular_error_relativo(resultado_teorico, resultado_numerico)
    return resultado_teorico, resultado_numerico, error_relativo

def suma_kahan(N):
    resultado_teorico = N/(N+1)
    resultado_numerico = 0
    compensacion = 0

    for k in range(1, N+1):
        termino_k = 1/(k*(k+1))
        y = termino_k - compensacion
        t = resultado_numerico + y
        compensacion = (t - resultado_numerico) - y
        resultado_numerico = t

    error_relativo = calcular_error_relativo(resultado_teorico, resultado_numerico)
    return resultado_teorico, resultado_numerico, error_relativo


def graficar_errores(valores_N):
    algoritmos = {
        "Mayor a menor": suma_mayor_a_menor,
        "Menor a mayor": suma_menor_a_mayor,
        "Orden aleatorio": suma_orden_aleatorio,
        "Kahan": suma_kahan,
    }

    errores = {nombre: [] for nombre in algoritmos}
    # random.seed(0)

    for N in valores_N:
        for nombre, algoritmo in algoritmos.items():
            _, _, error_relativo = algoritmo(N)
            errores[nombre].append(error_relativo)

    for nombre, valores_error in errores.items():
        plt.plot(
            valores_N,
            valores_error,
            marker=".",
            linestyle="None",
            label=nombre,
        )

    plt.xlabel("N")
    plt.ylabel("Error relativo")
    plt.title("Error relativo en función de N")
    plt.yscale("symlog", linthresh=1e-16)
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.show()


valores_N = range(10, 10001, 10)
graficar_errores(valores_N)

valores_N = range(1000, 10001, 1000)
graficar_errores(valores_N)

