
def cargar_matriz(n: int) -> list[list[int]]:
    """
    Carga una matriz de tamaño n x n con números enteros ingresados por teclado.
    Pre: n > 0
    Post: Devuelve una lista de listas (matriz) de n x n con valores enteros.
    """
    assert n > 0, "El tamaño de la matriz debe ser mayor que 0"

    matriz = []
    for fila_num in range(n):
        fila = []
        for col_num in range(n):
            num = int(input(f"Ingrese el elemento [{fila_num}][{col_num}]: "))
            fila.append(num)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz: list[list[int]]):
    """
    Imprime la matriz de manera legible.
    Pre: `matriz` es una lista de listas.
    Post: Imprime la matriz en la consola. No modifica la matriz.
    """
    for fila in matriz:
        print(fila)
    print()


def ordenar_filas(matriz: list[list[int]]):
    """
    Ordena cada fila de la matriz en forma ascendente.
    Pre: `matriz` es una lista de listas de números.
    Post: La matriz es modificada in-place. Cada fila queda ordenada ascendentemente.
    """
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz: list[list[int]], f1: int, f2: int):
    """
    Intercambia dos filas dadas.
    Pre: `matriz` es una lista de listas. 0 <= f1, f2 < len(matriz).
    Post: La matriz es modificada in-place, intercambiando las filas f1 y f2.
    """
    assert 0 <= f1 < len(matriz) and 0 <= f2 < len(matriz), "Índices fuera de rango"
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]


def intercambiar_columnas(matriz: list[list[int]], c1: int, c2: int):
    """
    Intercambia dos columnas dadas.
    Pre: `matriz` es una matriz cuadrada. 0 <= c1, c2 < len(matriz).
    Post: La matriz es modificada in-place, intercambiando las columnas c1 y c2.
    """
    n = len(matriz)
    assert 0 <= c1 < n and 0 <= c2 < n, "Índices fuera de rango"
    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]


def trasponer_matriz(matriz: list[list[int]]):
    """
    Traspone la matriz (intercambia Aij con Aji).
    Pre: `matriz` es una matriz cuadrada.
    Post: La matriz es modificada in-place, convirtiéndose en su transpuesta.
    """
    for i, fila in enumerate(matriz):
        for j, _ in enumerate(fila[i + 1:], start=i + 1):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila.
    Pre: `matriz` es una lista de listas. 0 <= fila < len(matriz). La fila no debe estar vacía.
    Post: Devuelve un float con el promedio de la fila. No modifica la matriz.
    """
    assert 0 <= fila < len(matriz), "Número de fila inválido"
    return sum(matriz[fila]) / len(matriz[fila])


def porcentaje_impares_columna(matriz: list[list[int]], columna: int) -> float:
    """
    Calcula el porcentaje de elementos impares en una columna.
    Pre: `matriz` es una matriz cuadrada de enteros. 0 <= columna < len(matriz).
    Post: Devuelve un float con el porcentaje de impares en la columna. No modifica la matriz.
    """
    n = len(matriz)
    assert 0 <= columna < n, "Número de columna inválido"
    impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)
    return (impares / n) * 100


def es_simetrica_diagonal_principal(matriz: list[list[int]]) -> bool:
    """
    Determina si la matriz es simétrica respecto a la diagonal principal.
    Pre: `matriz` es una matriz cuadrada.
    Post: Devuelve True si es simétrica, False en caso contrario. No modifica la matriz.
    """
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila[i + 1:], start=i + 1):
            if valor != matriz[j][i]:
                return False
    return True


def es_simetrica_diagonal_secundaria(matriz: list[list[int]]) -> bool:
    """
    Determina si la matriz es simétrica respecto a la diagonal secundaria.
    Pre: `matriz` es una matriz cuadrada.
    Post: Devuelve True si es simétrica, False en caso contrario. No modifica la matriz.
    """
    n = len(matriz)
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor != matriz[n - j - 1][n - i - 1]:
                return False
    return True


def columnas_palindromas(matriz: list[list[int]]) -> list[int]:
    """
    Devuelve una lista con los números de las columnas que son palíndromas.
    Pre: `matriz` es una matriz cuadrada.
    Post: Devuelve una lista de enteros con los índices de las columnas palíndromas.
    """
    n = len(matriz)
    palindromas = []
    for col_idx in range(n):
        columna = [fila[col_idx] for fila in matriz]
        if columna == columna[::-1]:
            palindromas.append(col_idx)
    return palindromas


# ---------------- MENÚ PRINCIPAL ---------------- #

def main():
    """Función principal que ejecuta el menú del programa de operaciones."""
    n = int(input("Ingrese el tamaño N de la matriz: "))
    matriz = cargar_matriz(n)

    # ... (El resto del menú principal no cambia)
    while True:
        print("\n=== MENÚ DE OPERACIONES CON MATRICES ===")
        print("1. Mostrar matriz")
        print("2. Ordenar filas")
        print("3. Intercambiar filas")
        print("4. Intercambiar columnas")
        print("5. Trasponer matriz")
        print("6. Calcular promedio de una fila")
        print("7. Calcular % de impares en una columna")
        print("8. Verificar simetría diagonal principal")
        print("9. Verificar simetría diagonal secundaria")
        print("10. Mostrar columnas palíndromas")
        print("0. Salir")

        op = int(input("Seleccione una opción: "))

        if op == 0:
            print("Fin del programa.")
            break

        elif op == 1:
            print("\nMatriz actual:")
            mostrar_matriz(matriz)

        elif op == 2:
            ordenar_filas(matriz)
            print("Filas ordenadas correctamente.")
            mostrar_matriz(matriz)

        elif op == 3:
            f1 = int(input("Ingrese el número de la primera fila: "))
            f2 = int(input("Ingrese el número de la segunda fila: "))
            intercambiar_filas(matriz, f1, f2)
            print("Filas intercambiadas.")
            mostrar_matriz(matriz)

        elif op == 4:
            c1 = int(input("Ingrese el número de la primera columna: "))
            c2 = int(input("Ingrese el número de la segunda columna: "))
            intercambiar_columnas(matriz, c1, c2)
            print("Columnas intercambiadas.")
            mostrar_matriz(matriz)

        elif op == 5:
            trasponer_matriz(matriz)
            print("Matriz traspuesta:")
            mostrar_matriz(matriz)

        elif op == 6:
            f = int(input("Ingrese el número de la fila: "))
            print(f"Promedio de la fila {f}: {promedio_fila(matriz, f)}")

        elif op == 7:
            c = int(input("Ingrese el número de la columna: "))
            print(f"Porcentaje de impares en columna {c}: {porcentaje_impares_columna(matriz, c)}%")

        elif op == 8:
            if es_simetrica_diagonal_principal(matriz) == True:
                print("La matriz es simétrica respecto a la diagonal principal.")
            else:
                print("La matriz no es simétrica respecto a la diagonal principal.")

        elif op == 9:
            if es_simetrica_diagonal_secundaria(matriz) == True:
                print("La matriz es simétrica respecto a la diagonal secundaria.")
            else:
                print("La matriz no es simétrica respecto a la diagonal secundaria.")

        elif op == 10:
            print("Columnas palíndromas:", columnas_palindromas(matriz))

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()