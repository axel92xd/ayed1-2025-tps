def contar_vocales(palabra: str) -> dict:
    """
    Recibe una palabra y cuenta cuántas veces aparece cada vocal.
    
    Pre:  Recibe un string (palabra).
    Post: Devuelve un diccionario donde las claves son las vocales
          encontradas y los valores son su conteo.
    """
    
    # Definimos las vocales que nos interesan
    vocales = "aeiouáéíóú"
    
    conteo_vocales = {} 
    
    # Convertimos la palabra a minúscula para no diferenciar
    for letra in palabra.lower():
        
        if letra in vocales:
            
            # Busca 'letra' en el diccionario. Si no la encuentra, devuelve 0. Luego le suma 1.
            conteo_vocales[letra] = conteo_vocales.get(letra, 0) + 1
            
    return conteo_vocales

    
def main():
    
    try:
        frase = input("Ingrese una frase: ")
        
        # Limpiamos la frase (simple, solo quitamos comas y puntos)
        frase_limpia = frase.replace(",", "").replace(".", "")
        
        # Separamos la frase en una lista de palabras
        palabras = frase_limpia.split()
        
        if not palabras:
            print("No se ingresaron palabras.")
        else:
            for p in palabras:
                resultado_dic = contar_vocales(p)
                print(f"Palabra: '{p}' -> Vocales: {resultado_dic}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()