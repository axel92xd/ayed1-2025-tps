import random

def juego_adivinar_numero():
    """
    Juego de adivinar un número entre 1 y 500.
    Maneja ingresos no numéricos como un intento fallido.
    
    Pre:  El usuario debe ingresar números por teclado.
    Post: Guía al usuario (mayor/menor) hasta que adivine.
          Al adivinar, imprime el número total de intentos.
    """
    # Generamos el número al azar
    numero_secreto = random.randint(1, 500)
    intentos = 0
    adivinado = False
    
    print("He pensado un número entre 1 y 500. ¡Intenta adivinarlo!")
    
    while not adivinado:
        try:
            entrada_str = input(f"Intento #{intentos + 1}: ")
            # Intentamos convertir. Fallará si ingresa "abc"
            entrada_num = int(entrada_str)
            
        except ValueError:
            print("Error: ¡Eso no es un número! Cuenta como un intento.")
            intentos += 1
            
        # Si el try tuvo éxito, contamos el intento
        intentos += 1
        
        if entrada_num < numero_secreto:
            print("El número secreto es MÁS GRANDE.")
        elif entrada_num > numero_secreto:
            print("El número secreto es MÁS PEQUEÑO.")
        else:
            adivinado = True
            
    print(f"\n¡Felicitaciones! Adivinaste el número {numero_secreto} en {intentos} intentos.")

def main():
    """
    Programa principal para probar la función juego_adivinar_numero.
    Pre: No recibe parámetros.
    Post: Inicia el juego de adivinar el número.
    """
    juego_adivinar_numero()

if __name__ == "__main__":
    main()