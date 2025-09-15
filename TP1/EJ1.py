def mayor_unico (numero1: int, numero2: int, numero3: int) -> int:
    """
    Devuelve el mayor numero entre 3 numeros
    Pre: numero1,numero2,numero3 son enteros positivos
    Post: devuelve el mayor unico, si no existe un mayor unico, devuelve -1
    """
    #Asserts
    assert isinstance(numero1,int) and numero1 > 0, f"{numero1} debe ser un entero positivo"
    assert isinstance(numero2,int) and numero2 > 0, f"{numero1} debe ser un entero positivo"
    assert isinstance(numero3,int) and numero3 > 0, f"{numero1} debe ser un entero positivo"

    
    if numero1 == numero2:
        if numero == numero3: 
            return -1
    else:
        return max(numero1,numero2,numero3)

#Funcion
def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    numero3 = int(input("Ingrese el tercer numero: "))

    resultado = mayor_unico(numero1,numero2,numero3)

    if resultado == -1:
        print("No existe un mayor unico")
    else:
        print(f"El numero mayor unico es: {resultado}")

if __name__ == "__main__":
    main()
    
        