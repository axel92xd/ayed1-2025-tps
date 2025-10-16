
# Utilizando rebanadas
def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena utilizando rebanadas.

    Pre: cadena (str): La cadena original.
         posicion (int): El índice de inicio de la subcadena a eliminar.
         cantidad (int): El número de caracteres a eliminar.
    Post: (str): La cadena resultante tras la eliminación.
    """
    parte_inicial = cadena[:posicion]
    parte_final = cadena[posicion + cantidad:]
    return parte_inicial + parte_final

# Sin utilizar rebanadas 
def eliminar_subcadena_ciclo(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena utilizando un ciclo, sin rebanadas.

    Pre: cadena (str): La cadena original. 
         posicion (int): El índice de inicio de la subcadena a eliminar.
         cantidad (int): El número de caracteres a eliminar.
    Post: (str): La cadena resultante tras la eliminación.
    """
    cadena_resultado = ""
    for i, caracter in enumerate(cadena):
        # Se añade el caracter solo si su índice está fuera del rango a eliminar
        if not (posicion <= i < posicion + cantidad):
            cadena_resultado += caracter
    return cadena_resultado

def main():
    """
    Función principal para eliminar una subcadena de una cadena dada.
    """
    cadena_ejemplo = "La materia se llama Programación II"
    print(f"Cadena de ejemplo: '{cadena_ejemplo}'")

    try:
        pos = int(input("Ingrese la posición inicial a eliminar: "))
        cant = int(input("Ingrese la cantidad de caracteres a eliminar: "))

        print("\nResultados:")
        resultado_a = eliminar_subcadena_rebanadas(cadena_ejemplo, pos, cant)
        print(f"  a) Usando rebanadas: '{resultado_a}'")

        resultado_b = eliminar_subcadena_ciclo(cadena_ejemplo, pos, cant)
        print(f"  b) Sin usar rebanadas: '{resultado_b}'")

    except ValueError:
        print("Error: La posición y la cantidad deben ser números enteros.")

if __name__ == "__main__":
    main()