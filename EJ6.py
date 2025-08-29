def concatenar(num1: int, num2: int) -> int:
    """
    Contrato General
    Concatena dos numeros enteros que recibe del usuario
    Pre: Recibe dos numeros enteros. num1,num2 son numeros positivos
    Post: Devuelve un numero entero concatenado por los dos numeros anteriores
    """
    assert isinstance(num1, int) and num1 > 0, f"{num1} debe ser un entero positivo"
    assert isinstance(num2, int) and num2 > 0, f"{num2} debe ser un entero positivo"

    return int("".join([str(num1), str(num2)]))


def main():
    num1  = int(input("Ingrese un numero: "))
    num2  = int(input("Ingrese un segundo numero: "))
    
    num3 = concatenar(num1,num2)
    
    print(f"El numero concatenado es: {num3}")
    
if __name__ == "__main__":
    main()


