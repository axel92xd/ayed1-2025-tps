"""
Programa para generar matrices N x N con patrones predefinidos.
El usuario ingresa el tamaño N y elige el patrón a generar.
"""

# ----------------- FUNCIÓN UTILITARIA ----------------- #

def mostrar_matriz(matriz: list[list[int]]):
    """
    Imprime la matriz de manera legible, alineando los números.
    Pre: `matriz` es una lista de listas.
    Post: Imprime la matriz en la consola de forma alineada. No modifica la matriz.
    """
    if not matriz:
        print("La matriz está vacía.")
        return
    max_len = max(len(str(num)) for fila in matriz for num in fila)
    
    for fila in matriz:
        print(" ".join(f"{num:<{max_len}}" for num in fila))
    print()


# ----------------- FUNCIONES DE GENERACIÓN DE MATRICES ----------------- #

def generar_matriz_a(n: int) -> list[list[int]]:
    """
    Genera una matriz con números impares en la diagonal principal.
    Pre: n > 0.
    Post: Devuelve una matriz n x n con los primeros n impares en la diagonal principal.
    """
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][i] = 2 * i + 1
    return matriz


def generar_matriz_b(n: int) -> list[list[int]]:
    """
    Genera una matriz con potencias de 3 en la diagonal secundaria.
    Pre: n > 0.
    Post: Devuelve una matriz n x n con potencias de 3 en la diagonal secundaria.
    """
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                matriz[i][j] = 3**(n - 1 - i)
    return matriz


def generar_matriz_c(n: int) -> list[list[int]]:
    """
    Genera una matriz con el triángulo inferior relleno por filas.
    Pre: n > 0.
    Post: Devuelve una matriz n x n con el triángulo inferior relleno.
    """
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j <= i:
                matriz[i][j] = n - i
    return matriz


def generar_matriz_d(n: int) -> list[list[int]]:
    """
    Genera una matriz con filas de potencias de 2 decrecientes.
    Pre: n > 0.
    Post: Devuelve una matriz n x n donde cada fila i contiene el valor 2**(n-1-i).
    """
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        valor_fila = 2**(n - 1 - i)
        for j in range(n):
            matriz[i][j] = valor_fila
    return matriz


def generar_matriz_e(n: int) -> list[list[int]]:
    """
    Genera una matriz con un patrón de 'tablero de ajedrez'.
    Pre: n > 0.
    Post: Devuelve una matriz n x n con números consecutivos en las posiciones donde i+j es impar.
    """
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                matriz[i][j] = contador
                contador += 1
    return matriz


def generar_matriz_f(n: int) -> list[list[int]]:
    """
    Genera una matriz con el triángulo superior-derecho relleno.
    Pre: n > 0.
    Post: Devuelve una matriz n x n con el triángulo superior-derecho relleno con números consecutivos.
    """
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if i + j >= n - 1:
                matriz[i][j] = contador
                contador += 1
    return matriz


def generar_matriz_g(n: int) -> list[list[int]]:
    """
    Genera una matriz con un recorrido en espiral.
    Pre: n > 0.
    Post: Devuelve una matriz n x n rellenada con números consecutivos en espiral.
    """
    matriz = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    contador = 1
    
    while top <= bottom and left <= right:
        # Rellenar fila superior
        for j in range(left, right + 1):
            matriz[top][j] = contador
            contador += 1
        top += 1
        # (El resto de la lógica de la espiral sigue aquí...)
        for i in range(top, bottom + 1):
            matriz[i][right] = contador
            contador += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matriz[bottom][j] = contador
                contador += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = contador
                contador += 1
            left += 1
    return matriz

def generar_matriz_h(n: int) -> list[list[int]]:
    """
    Genera una matriz rellenada por anti-diagonales.
    Pre: n > 0.
    Post: Devuelve una matriz n x n rellenada con números consecutivos por anti-diagonales.
    """
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for suma_indices in range(2 * n - 1):
        for i in range(suma_indices + 1):
            j = suma_indices - i
            if 0 <= i < n and 0 <= j < n:
                matriz[i][j] = contador
                contador += 1
    return matriz


def generar_matriz_i(n: int) -> list[list[int]]:
    """
    Genera una matriz rellenada por anti-diagonales en zig-zag.
    Pre: n > 0.
    Post: Devuelve una matriz n x n rellenada en zig-zag con números consecutivos.
    """
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for suma_indices in range(2 * n - 1):
        if suma_indices % 2 == 0:
            for i in range(suma_indices, -1, -1):
                j = suma_indices - i
                if 0 <= i < n and 0 <= j < n:
                    matriz[i][j] = contador
                    contador += 1
        else:
            for i in range(suma_indices + 1):
                j = suma_indices - i
                if 0 <= i < n and 0 <= j < n:
                    matriz[i][j] = contador
                    contador += 1
    return matriz


# ----------------- MENÚ PRINCIPAL ----------------- #

def main():
    """Función principal que ejecuta el menú del programa de generación."""
    # ... (El menú principal no cambia)
    while True:
        try:
            n = int(input("Ingrese el tamaño N de la matriz (N > 0): "))
            if n > 0:
                break
            else:
                print("Error: El tamaño debe ser un número entero positivo.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
    
    generadores = {
        'a': generar_matriz_a, 'b': generar_matriz_b, 'c': generar_matriz_c,
        'd': generar_matriz_d, 'e': generar_matriz_e, 'f': generar_matriz_f,
        'g': generar_matriz_g, 'h': generar_matriz_h, 'i': generar_matriz_i,
    }
    
    while True:
        print("\n=== MENÚ DE GENERACIÓN DE MATRICES ===")
        # ... (las opciones del menú siguen igual)
        op = input("Seleccione una opción: ").lower()
        if op == 'q':
            break
        if op in generadores:
            matriz_generada = generadores[op](n)
            print(f"\n--- Matriz '{op.upper()}' de tamaño {n}x{n} ---")
            mostrar_matriz(matriz_generada)
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()