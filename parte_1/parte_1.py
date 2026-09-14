
import matplotlib.pyplot as plt

def suma(N, b):
    
    suma_1 = 0
    suma_2 = 0
    suma_3 = 0
    
    for k in range(1, N+1):
        
        termino_k_suma_1 = (1 + b**k - b**k)
        termino_k_suma_2 = (1 + b**k) - b**k
        termino_k_suma_3 = (1 - b**k) + b**k
        
        suma_1 += termino_k_suma_1
        suma_2 += termino_k_suma_2
        suma_3 += termino_k_suma_3
        
    return [suma_1, suma_2, suma_3]

# print(suma(34, 3.0))

def graficar_sumas(valores_N, valores_b):
    figura, ejes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)

    for eje, b in zip(ejes.flat, valores_b):
        valores_N_validos = []
        resultados = []

        for N in valores_N:
            try:
                resultado = suma(N, b)
            except OverflowError:
                break

            valores_N_validos.append(N)
            resultados.append(resultado)

        for indice, nombre_suma in enumerate((r"$X_N$", r"$Y_N$", r"$Z_N$")):
            valores = [resultado[indice] for resultado in resultados]
            eje.plot(valores_N_validos, valores, label=nombre_suma)

        eje.set_title(f"b = {b}")
        eje.set_xlabel("N")
        eje.set_ylabel("Resultado")
        eje.grid(True)
        eje.legend()

    primer_N = min(valores_N)
    ultimo_N = max(valores_N)
    figura.suptitle(f"Resultado de las sumatorias para N = {primer_N} hasta N = {ultimo_N}")
    figura.tight_layout()
    plt.show()


valores_N = range(1, 1001)
valores_b = [2, 3, 5, 10]
graficar_sumas(valores_N, valores_b)

valores_b = [2.0, 3.0, 5.0, 10.0]
graficar_sumas(valores_N, valores_b)