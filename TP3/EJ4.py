import random as rn

def imprimir_matriz_produccion(matriz: list[list[int]], titulo: str = "Matriz"):
    """
    Muestra la matriz de producción de forma alineada.
    
    Pre: `matriz` es una lista de listas de enteros.
    Post: Imprime la matriz en la consola.
    """
    print(f"\n--- {titulo} ---")
    dias_cabecera = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
    
    print("        |" + "".join(f"{dia:>5}" for dia in dias_cabecera))
    print("-" * 45)
    
    if not matriz:
        print("La matriz está vacía.")
        return

    for i, fila in enumerate(matriz):
        print(f"Fábrica {i+1:2} |" + "".join(f"{num:>5}" for num in fila))
    print()

def matriz_random(cantidad:int)->list[list[int]]:
    """
    Crea una matriz de producción (fábricas x 6 días) con valores aleatorios [0, 150].
    
    Pre: `cantidad` (int) es el número de fábricas (> 0).
    Post: Retorna una matriz (list[list[int]]) de tamaño `cantidad` x 6.
    """
    max_pro = 150
    dias_semana = 6
    return [[rn.randint(0, max_pro) for _ in range(dias_semana)] for _ in range(cantidad)]

def fabricadas_por_fabrica(matriz:list[list[int]]) -> list[int]:
    """
    Calcula el total de bicicletas fabricadas por cada planta.
    
    Pre: `matriz` es una lista de listas de enteros.
    Post: Retorna una lista con la suma total de producción por cada fila (fábrica).
    """
    return [sum(fila) for fila in matriz]
    
def mayor_produccion(matriz:list[list[int]]) -> tuple[int, int, int]:
    """
    Encuentra la cantidad máxima producida en un solo día, su día y fábrica.
    
    Pre: `matriz` no debe estar vacía.
    Post: Retorna: (cantidad_maxima, indice_dia, indice_fabrica).
    """
    maximo_dia_ventas = -1
    indice_dia = -1
    indice_fabrica = -1
    
    for i, fila in enumerate(matriz):
        for j, produccion_dia in enumerate(fila):
            if produccion_dia > maximo_dia_ventas:
                maximo_dia_ventas = produccion_dia
                indice_dia = j         
                indice_fabrica = i     

    return maximo_dia_ventas, indice_dia, indice_fabrica

def dia_mas_productivo(matriz:list[list[int]]) -> int:
    """
    Calcula el índice del día con la mayor producción total combinada.
    
    Pre: Cada fila de la matriz debe tener 6 elementos (días).
    Post: Retorna un entero (índice 0-5) del día más productivo.
    """
    ventas = [0] * 6 # Suma de ventas para 6 días
    
    for fila in matriz:
        # Suma la producción de cada día de la fábrica actual a la lista de totales.
        for i, produccion_dia in enumerate(fila):  
            ventas[i] += produccion_dia
            
    # Encuentra el índice del valor máximo
    return ventas.index(max(ventas))

def lista_por_comprension(matriz:list[list[int]])->list[int]:
    """
    Genera una lista con la menor cantidad fabricada por día en cada fábrica.
    
    Pre: `matriz` no debe tener filas vacías.
    Post: Retorna una lista con el valor mínimo de cada fila (fábrica).
    """
    # Simplificado a una única línea con list comprehension y min()
    return [min(x) for x in matriz]

def main () ->None:
    """
    Función principal del EJERCICIO 4. Controla el flujo de ejecución.
    
    Pre: No recibe parámetros.
    Post: Imprime el análisis de producción.
    """
    dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
    
    # Asumimos que el usuario ingresa un número entero (sin manejo de excepciones)
    cantidad = int(input("Ingrese cuántas fábricas tiene: "))
    
    if cantidad <= 0:
        print("El número de fábricas debe ser mayor a cero. Terminando programa.")
        return

    matriz = matriz_random(cantidad)
    imprimir_matriz_produccion(matriz, "Producción Semanal de Bicicletas")

    print("\n--- b. Producción Total por Fábrica ---")
    totales_por_fabrica = fabricadas_por_fabrica(matriz)
    for i, total in enumerate(totales_por_fabrica):
        print(f"Fábrica {i+1}: {total} unidades")

    print("\n--- c. Récord de Producción en un Día ---")
    max_ventas, indice_dia, indice_fabrica = mayor_produccion(matriz)
    print(f"La mayor producción fue de {max_ventas} unidades.")
    print(f"Ocurrió el día {dias[indice_dia]} en la Fábrica {indice_fabrica + 1}.")

    print("\n--- d. Día Más Productivo de la Semana ---")
    dia_indice = dia_mas_productivo(matriz)
    print(f"El día más productivo (total combinado) es el {dias[dia_indice]}.")

    print("\n--- e. Mínima Producción Diaria por Fábrica (Lista por Comprensión) ---")
    minimos = lista_por_comprension(matriz)
    print("Mínimos por fábrica:", minimos)

if __name__ == "__main__":
    main()