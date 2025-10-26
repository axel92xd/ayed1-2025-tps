# --- Definición de la Función Lógica ---
def crear_baraja_espanola() -> list[str]:
    """
    Crea una lista con los 48 naipes de la baraja española usando una lista por comprensión.

    Pre: Ninguna.
    Post: (list[str]): Una lista de cadenas con todos los naipes.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    numeros = range(1, 13) # Del 1 al 12
    
    # Esta es la lista por comprensión anidada.
    # Por cada palo en la lista de palos recorre cada número en el rango de números.
    baraja = [f"{num} {palo}" for palo in palos for num in numeros]
    
    return baraja

def main():
    """
    Función principal para crear e imprimir la baraja española.
    """
    
    baraja = crear_baraja_espanola()
    
    # Imprimimos la baraja
    print(f"Total de naipes: {len(baraja)}")
    print("\nLista de naipes:")
    for carta in baraja:
        print(carta)

if __name__ == "__main__":
    main()