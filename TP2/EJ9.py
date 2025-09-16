# ==================== Ejercicio 9 ====================
def multiplos_7(A: int, B: int) -> list[int]:
    """
    Genera lista de números entre A y B (inclusive) que sean múltiplos de 7 pero no de 5.
    
    Pre: A y B enteros, A <= B
    Post: Lista de enteros que cumplen la condición
    """
    assert isinstance(A, int) and isinstance(B, int) and A <= B, "A y B deben ser enteros con A <= B"
    lista = [x for x in range(A, B + 1) if x % 7 == 0 and x % 5 != 0]
    return lista

A = int(input("Ingrese A: "))
B = int(input("Ingrese B: "))

print(multiplos_7(A, B))
