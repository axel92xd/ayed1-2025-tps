def generar_diccionario_cuadrados():
    """
    Genera un diccionario donde las claves son números (1-20)
    y los valores son sus cuadrados.
    
    Pre:  Ninguna.
    Post: Imprime el diccionario resultante.
    """
    
    diccionario_cuadrados = {} # Creamos un diccionario vacío
    
    for numero in range(1, 21):
     
        diccionario_cuadrados[numero] = numero ** 2
        

    print(diccionario_cuadrados)

def main():
    """
    Función principal para ejecutar el ejercicio.
    Pre:  Ninguna.
    Post: Ejecuta la generación del diccionario de cuadrados.
    """
    generar_diccionario_cuadrados()

if __name__ == "__main__":
    main()