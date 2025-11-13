def encajan_domino(ficha1: tuple, ficha2: tuple) -> bool:
    """
    Indica si dos fichas de dominó encajan (tienen un número en común).
    Resuelto usando la intersección de conjuntos (sets).
    
    Pre:  ficha1 (num1, num2), ficha2 (num3, num4)
    Post: Devuelve True si encajan, False si no.
    """
    
    # Convertimos las tuplas en conjuntos (sets)
    set_ficha1 = set(ficha1)
    set_ficha2 = set(ficha2)
    
    # Calculamos la intersección (los números que están en AMBOS sets)
    #    El operador '&' es la intersección
    interseccion = set_ficha1 & set_ficha2
    
    # Si la intersección NO está vacía, significa que encajan
    #    bool() convierte un set vacío a False y uno con datos a True
    return bool(interseccion)

if __name__ == "__main__":
    
    
    f1 = (3, 4)
    f2 = (5, 4) 
    f3 = (1, 2) 
    f4 = (6, 6) 
    f5 = (2, 6) 
    
    print(f"{f1} y {f2} -> {encajan_domino(f1, f2)}") 
    print(f"{f1} y {f3} -> {encajan_domino(f1, f3)}") 
    print(f"{f3} y {f5} -> {encajan_domino(f3, f5)}") 
    print(f"{f4} y {f5} -> {encajan_domino(f4, f5)}") 
    
    try:
        print("\n Prueba Manual")
        n1 = int(input("Ficha 1, número A: "))
        n2 = int(input("Ficha 1, número B: "))
        n3 = int(input("Ficha 2, número A: "))
        n4 = int(input("Ficha 2, número B: "))
        
        mi_ficha1 = (n1, n2)
        mi_ficha2 = (n3, n4)
        
        if encajan_domino(mi_ficha1, mi_ficha2):
            print("Las fichas encajan")
        else:
            print("Las fichas no encajan.")
            
    except ValueError:
        print("Error: Ingrese solo números.")