def gestionar_precios():
    """
    Programa principal del ejercicio 12.
    1. Crea un diccionario de precios.
    2. Incrementa el precio de los cuadernos en 15%.
    3. Imprime el listado completo.
    4. Indica el ítem más costoso.
    Pre:  Ninguna.
    Post: Muestra el listado actualizado y el ítem más costoso.
    """
    
    precios_libreria = {
        "Lápiz": 150.00,
        "Goma de borrar": 100.50,
        "Cuaderno A4 (rayado)": 1200.00,
        "Regla 20cm": 250.00,
        "Cuaderno Oficio (cuadriculado)": 1500.00,
        "Resaltador": 300.75
    }
    
    print(f"Precios Originales: {precios_libreria}")

    # Incrementar precios de cuadernos
    # (Iteramos sobre una copia .items() para poder modificar el original)
    for item, precio in precios_libreria.items():
        
        # Si la palabra "cuaderno" está en el nombre
        if "cuaderno" in item.lower():
            
            nuevo_precio = precio * 1.15 # Incrementamos 15%
            
            # Actualizamos el precio en el diccionario
            precios_libreria[item] = round(nuevo_precio, 2) # Redondeamos a 2 decimales

    # Imprimir el listado actualizado
    print("\n Listado de Precios Actualizado (15% en cuadernos)")
    for item, precio in precios_libreria.items():
        print(f"  - {item}: ${precio:.2f}")

    # Indicar el ítem más costoso
    if precios_libreria: # Verificamos que el diccionario no esté vacío
        
        # (item) que tiene el valor (precio) más alto.
        item_max = max(precios_libreria, key=precios_libreria.get)
        precio_max = precios_libreria[item_max]
        
        print("\n Ítem más costoso")
        print(f"El ítem más costoso es: {item_max} (${precio_max:.2f})")
    
    else:
        print("\nNo hay precios cargados.")

if __name__ == "__main__":
    gestionar_precios()