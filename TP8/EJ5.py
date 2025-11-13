def son_ortogonales(vector_a: tuple, vector_b: tuple) -> bool:
    """
    Calcula si dos vectores (representados como tuplas) son ortogonales.
    Dos vectores son ortogonales si su producto escalar es 0.
    
    Pre:  vector_a (tupla de 2 números, ej: (x1, y1))
          vector_b (tupla de 2 números, ej: (x2, y2))
    Post: Devuelve True si el producto escalar (x1*x2 + y1*y2) es 0.
          Devuelve False en caso contrario o si hay un error.
    """
    try:
        # "Desempaquetamos" las tuplas para obtener los componentes
        (x1, y1) = vector_a
        (x2, y2) = vector_b
        
        # Calculamos el producto escalar 
        producto_escalar = (x1 * x2) + (y1 * y2)
        
        # Devolvemos la comparación (True o False)
        return producto_escalar == 0
        
    except (ValueError, TypeError):
        # Si las tuplas no tienen 2 elementos o no son numéricos
        print("Error: Los vectores deben ser tuplas de dos números (x, y).")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

def pedir_vector(nombre_vector: str) -> tuple:
    """
    Función auxiliar para pedir un vector (par ordenado) al usuario.
    
    Pre:  nombre_vector (str) - El nombre para mostrar (ej: "A")
    Post: Devuelve una tupla (x, y) con números flotantes.
    """
    print(f"\n--- Ingresando Vector {nombre_vector} ---")
    while True:
        try:
            # Pedimos números reales (
            x = float(input(f"Ingrese componente X para {nombre_vector}: "))
            y = float(input(f"Ingrese componente Y para {nombre_vector}: "))
            return (x, y)
        except ValueError:
            print("Error: Ingrese solo números (enteros o decimales).")



def main():
        """
        Función principal para ejecutar el ejercicio.
        Pre:  Ninguna.
        Post: Pide dos vectores y muestra si son ortogonales.

        """  
        A = (2, 3)
        B = (-3, 2)
        print(f"\nPrueba 1:")
        print(f"Vector A: {A}")
        print(f"Vector B: {B}")
        print(f"¿Son ortogonales? -> {son_ortogonales(A, B)}") 

        C = (5, 4)
        D = (1, 1)
        print(f"\nPrueba 2 (No ortogonales):")
        print(f"Vector C: {C}")
        print(f"Vector D: {D}")
        print(f"¿Son ortogonales? -> {son_ortogonales(C, D)}") 
    
        print("\n--- Prueba Manual ---")
        v1 = pedir_vector("V1")
        v2 = pedir_vector("V2")
    
        if son_ortogonales(v1, v2):
            print(f"\nResultado: Los vectores {v1} y {v2} SÍ son ortogonales.")
        else:
            print(f"\nResultado: Los vectores {v1} y {v2} NO son ortogonales.")

if __name__ == "__main__":
    main()