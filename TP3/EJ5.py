import random as rn

# --- FUNCIONES DE LA SALA ---

def cargar_sala(filas:int, columnas:int)->list[list[int]]:
    """
    Crea una matriz con butacas ocupadas (1) o libres (0) de forma aleatoria.
    
    Pre: Recibe las dimensiones (filas, columnas) de la sala (> 0).
    Post: Retorna la matriz de butacas (list[list[int]]).
    """
    matriz = []
    for f in range(filas):
        fila = []
        # El 0 o 1 representa el estado: 0=Libre, 1=Ocupado/Reservado
        for num in range(columnas):
            fila.append(rn.randint(0,1))
        matriz.append(fila)
    return matriz

def mostrar_butacas(matriz: list[list[int]]) -> None:
    """
    Muestra por pantalla el estado de las butacas (0: Libre, 1: Ocupada).
    
    Pre: Recibe la matriz de butacas.
    Post: Imprime la matriz en la consola.
    """
    if not matriz:
        print("La sala está vacía.")
        return
    
    print("\n--- Estado Actual de la Sala (0: Libre, 1: Ocupada) ---")
    
    # Imprimir cabecera de butacas (columnas)
    num_butacas = len(matriz[0])
    print(" Butaca " + "".join(f"{j+1:>4}" for j in range(num_butacas)))
    print(" Fila      " + "-" * (4 * num_butacas + 2))

    # Imprimir filas
    for i, fila in enumerate(matriz):
        print(f" {i+1:>4}:" + "".join(f"{c:>4}" for c in fila))
    print()


def reservar(matriz: list[list[int]]) -> bool:
    """
    Solicita al usuario un número de asiento (secuencial, desde 1) e intenta reservarlo.
    
    Pre: Recibe la matriz de asientos.
    Post: Retorna True si la reserva es exitosa, False si está ocupado o no existe.
    """
    contador = 0
    
    try:
        reserva = int(input("Elija un asiento (contando desde la butaca 1). Las butacas '0' están libres: "))
    except ValueError:
        print("Error: La butaca debe ser un número entero.")
        return False
        
    if reserva <= 0:
        return False

    for i, f in enumerate(matriz):
        for i2, c in enumerate(f):
            contador += 1
            if contador == reserva:
                # Se encontró la butaca
                if c == 1:
                    print(f"Reserva fallida. El asiento {reserva} ya está ocupado (1).")
                    return False
                else:
                    matriz[i][i2] = 1 # Reservar
                    return True # Reservado
    

    print(f"Reserva fallida. El asiento {reserva} no existe en la sala.")
    return False

def butacas_libres(matriz:list[list[int]])->int:
    """
    Cuenta la cantidad de butacas libres (valor 0) en la sala.
    
    Pre: Recibe la matriz de asientos.
    Post: Retorna el número entero de asientos libres.
    """
    contador = 0
    for fila in matriz:
        for butaca in fila:
            if butaca == 0:
                contador += 1
    return contador

def butacas_contiguas(matriz:list[list[int]])->tuple[int, int]:
    """
    Busca la secuencia más larga de butacas libres contiguas en una misma fila.
    
    Pre: Recibe la matriz de asientos.
    Post: Retorna una tupla: (longitud_maxima, indice_de_la_fila).
    """
    contador_mas_largo = 0
    fila_record = -1
    
    for i, f in enumerate(matriz):
        contador = 0
        for c in f:
            if c == 0: # Butaca libre
                contador += 1
                if contador > contador_mas_largo:
                    contador_mas_largo = contador
                    fila_record = i # Guarda el índice de la fila
            else: # Butaca ocupada, la secuencia se rompe
                contador = 0
                
    return contador_mas_largo, fila_record
  
def main()->None:
    """
    Función principal del programa de reservas de cine.
    
    Pre: No recibe parámetros.
    Post: Muestra en pantalla el resultado de las operaciones.
    """
    print("--- GESTIÓN DE RESERVAS DE CINE ---")
    
    try:
        filas = int(input("Ingrese la cantidad de filas del cine (N):"))
        butacas = int(input("Ingrese cuantas butacas tiene cada fila (M):"))
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")
        return

    if filas > 0 and butacas > 0:
        print("Valores válidos. Cargando sala...")
        
        # 1. Cargar sala
        matriz = cargar_sala(filas, butacas)
        
        # 2. Mostrar estado ANTES de la reserva
        mostrar_butacas(matriz)
        
        # 3. Reservar
        if reservar(matriz):
            print("Asiento reservado con éxito!")
            
            # 4. Mostrar estado DESPUÉS de la reserva
            mostrar_butacas(matriz)
        else:
            print("No se pudo reservar el asiento.")
            
        # 5. Butacas libres
        print(f"La cantidad de butacas libres es de {butacas_libres(matriz)}")
        
        # 6. Butacas contiguas
        contador, fila_indice = butacas_contiguas(matriz)
        if contador > 0:
            print(f"La secuencia más larga de butacas libres es de {contador} y ocurre en la Fila {fila_indice + 1}")
        else:
            print("No hay butacas libres disponibles.")
    else:
        print("Las filas y butacas deben ser números positivos.")

if __name__ == "__main__":
    main()