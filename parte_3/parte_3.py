import math

import matplotlib.pyplot as plt

def calcular_error_relativo(teorico, numerico):
    if teorico == 0:
        return float('inf')  # Evitar división por cero
    return abs((teorico - numerico) / teorico)

def calcular_diferencia_absoluta(valor_1, valor_2):
    return abs(valor_1 - valor_2)

def suma_b(N):
    resultado_teorico = N/(N+1)
    resultado_1 = 0
    resultado_2 = 0
    
    for k in range(1, N+1):
        termino_k_1 = 1/(k*(k+1))
        termino_k_2 = (1/k) - (1/(k+1))
        
        resultado_1 += termino_k_1
        resultado_2 += termino_k_2

    error_relativo_1 = calcular_error_relativo(resultado_teorico, resultado_1)
    error_relativo_2 = calcular_error_relativo(resultado_teorico, resultado_2)
    return resultado_teorico, resultado_1, error_relativo_1, resultado_2, error_relativo_2

def suma_c(N):
    resultado_1 = 0
    resultado_2 = 0
    
    for k in range(1, N+1):
        termino_k_1 = 1/(math.sqrt(k**2 + 1) + k)
        termino_k_2 = math.sqrt(k**2 + 1) - k
        
        resultado_1 += termino_k_1
        resultado_2 += termino_k_2
        
    diferencia_absoluta = calcular_diferencia_absoluta(resultado_1, resultado_2)
    return resultado_1, resultado_2, diferencia_absoluta


valores_N = [1] + list(range(10, 10001, 10))
errores_1 = []
errores_2 = []

for N in valores_N:
    _, _, error_1, _, error_2 = suma_b(N)
    errores_1.append(error_1)
    errores_2.append(error_2)

plt.plot(
    valores_N,
    errores_1,
    marker=".",
    linestyle="None",
    label=r"$\frac{1}{k(k+1)}$",
)
plt.plot(
    valores_N,
    errores_2,
    marker=".",
    linestyle="None",
    label=r"$\frac{1}{k} - \frac{1}{k+1}$",
)
plt.xlabel("N")
plt.ylabel("Error relativo")
plt.title("Error relativo de la suma b")
plt.yscale("symlog", linthresh=1e-16)
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.show()


diferencias_absolutas = []

for N in valores_N:
    _, _, diferencia_absoluta = suma_c(N)
    diferencias_absolutas.append(diferencia_absoluta)

plt.figure()
plt.plot(
    valores_N,
    diferencias_absolutas,
    marker=".",
    linestyle="None",
    label="Diferencia absoluta",
)
plt.xlabel("N")
plt.ylabel("Diferencia absoluta")
plt.title("Diferencia absoluta entre los resultados de la suma C")
plt.yscale("symlog", linthresh=1e-16)
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.show()