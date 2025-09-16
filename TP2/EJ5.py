def ordenada(lista):
    """
    Devuelve True si la lista está ordenada en forma ascendente,
    False en caso contrario.
    Pre: lista es una lista de elementos comparables
    Post: devuelve un booleano
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def main():
    lista1 = [1, 2, 3]
    lista2 = ['b', 'a']
    lista3 = [10, 20, 20, 30]
    
    print(f"{lista1} -> {ordenada(lista1)}")
    print(f"{lista2} -> {ordenada(lista2)}")
    print(f"{lista3} -> {ordenada(lista3)}")


if __name__ == "__main__":
    main()
