import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return x**3 - 2*x**2 + 4*x - 8

def biseccion(a, b, tol):
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con la condición f(a) * f(b) < 0 en el intervalo dado.")
        return None
    
    iteraciones = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if funcion(c) == 0.0:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    
    raiz_aproximada = (a + b) / 2.0
    
    # Preguntar si desea ver la gráfica
    respuesta = input("¿Desea ver la gráfica de la función? (S/N): ").strip().upper()
    if respuesta == "S":
        graficar_funcion(a, b, raiz_aproximada)
    
    return raiz_aproximada, iteraciones

def graficar_funcion(a, b, raiz_aproximada):
    x = np.linspace(a, b, 100)
    y = funcion(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x) = x^3 - 2x^2 + 4x - 8")
    plt.axhline(0, color='r', linestyle='--', label='f(x) = 0')
    plt.axvline(raiz_aproximada, color='g', linestyle='--', label='Raíz Aproximada')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfica de la Función y Raíz Aproximada")
    plt.legend()
    plt.grid(True)
    plt.show()

a = 1.0
b = 3.0
tolerancia = 0.0001

raiz, num_iteraciones = biseccion(a, b, tolerancia)

if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")
    print(f"Número de iteraciones: {num_iteraciones}")
