import random
import tabulate

def imprimir_matriz(matriz: list[list[int]]):
    """
    Imprime la matriz de manera legible usando tabulate.
    Pre: matriz es una lista de listas de números.
    Post: Imprime la matriz en formato de cuadrícula en la consola.
    """
    if len(matriz) == 0:
        print("La matriz está vacía.")
        return
    
    # Usa tabulate para un formato profesional
    print(tabulate.tabulate(matriz, tablefmt="grid"))
    print()

def crear_matriz_sin_repetir(n: int) -> list[list[int]]:
    """
    Rellena una matriz de N x N con números enteros al azar únicos y utiliza el método de 'Barajar y Repartir' para asegurar unicidad y aleatoriedad.
    Pre: n (int) es el tamaño de la matriz (N > 0).
    Post: Retorna una lista de listas (matriz) de tamaño N x N. Los números están en el intervalo [0, N^2 - 1). **Ningún número se repite.**
    """
    # 1. Crear una lista con todos los números posibles del rango [0, N^2 - 1].
    total_numeros = n * n
    numeros_disponibles = list(range(total_numeros))
    
    # 2. Barajar (mezclar) la lista de forma aleatoria.
    random.shuffle(numeros_disponibles)
    
    # 3. Construir la matriz repartiendo la lista barajada en filas de N elementos.
    matriz = []
    for i in range(n):
        inicio = i * n
        fin = inicio + n
        fila = numeros_disponibles[inicio:fin]
        matriz.append(fila)
        
    return matriz

def main():
    """
    Función principal para ejecutar el ejercicio 3.
    
    Pre:No recibe parámetros.
    Post:Solicita el tamaño de la matriz al usuario, la genera e imprime. No devuelve ningún valor (None).
    """
    # Asumimos que la entrada es un entero (sin manejo de excepciones).
    n = int(input("Ingrese el tamaño de la matriz (N): "))

    if n > 0:
        matriz = crear_matriz_sin_repetir(n)
        print(f"\nMatriz de {n}x{n} generada con números únicos:")
        imprimir_matriz(matriz)
    else:
        print("El tamaño debe ser un número positivo.")

if __name__ == "__main__":
    main()