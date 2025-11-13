def eliminar_claves(mi_diccionario: dict, claves_a_eliminar: list) -> tuple:
    """
    Elimina un conjunto de claves de un diccionario.
    
    Pre:  Recibe un diccionario y una lista de claves (strings).
    Post: Devuelve una tupla: (el diccionario modificado, 
          la cantidad de claves que SÍ se eliminaron).
    """
    
    claves_eliminadas_contador = 0
    
    # Recorremos la LISTA de claves que queremos borrar
    for clave in claves_a_eliminar:
        
        # Usamos .pop(clave, None)
        # Intenta borrar la 'clave'. Si la encuentra, la borra y
        # devuelve el valor (que no será None).
        # Si NO la encuentra, devuelve None y no da error.
        valor_eliminado = mi_diccionario.pop(clave, None)
        
        # Si el valor no es None, significa que la clave existía
        # y fue eliminada exitosamente.
        if valor_eliminado is not None:
            claves_eliminadas_contador += 1
            
    return mi_diccionario, claves_eliminadas_contador


def main():
    
    # Diccionario inicial
    stock_productos = {
        "Manzana": 150,
        "Banana": 200,
        "Naranja": 300,
        "Pera": 100
    }
    
    # Lista de claves a eliminar
    # "Pera" existe, "Lápiz" no existe)
    lista_para_borrar = ["Banana", "Pera", "Lápiz"]
    
    print(f"Stock INICIAL: {stock_productos}")
    print(f"Claves a eliminar: {lista_para_borrar}")
    
    
    stock_actualizado, cantidad = eliminar_claves(stock_productos, lista_para_borrar)
    
    print(f"Stock FINAL: {stock_actualizado}")
    print(f"Cantidad de claves eliminadas: {cantidad}") # Debería ser 2

if __name__ == "__main__":
    main()