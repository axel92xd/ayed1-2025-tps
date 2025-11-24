def resto_recursivo(dividendo, divisor):
    """
    Calcula el resto de la división (dividendo % divisor) restando.
    Pre: dividendo y divisor son enteros, y divisor > 0.
    Post: Devuelve el resto de la división entre dividendo y divisor.
    """
    # Caso Base: Si el dividendo es menor que el divisor, 
    # ya no podemos restar más. Ese es el resto.
    if dividendo < divisor:
        return dividendo
    
    # Restamos el divisor una vez y volvemos a probar
    return resto_recursivo(dividendo - divisor, divisor)

def main():
    """
    Pregunta al usuario por el dividendo y el divisor, y muestra el resto de la
    división utilizando la función resto_recursivo.
    Pre: El usuario debe ingresar dos números enteros, donde el divisor es mayor que 0.
    Post: Muestra el resto de la división entre el dividendo y el divisor.
    """
    dividendo = int(input("Ingrese el dividendo (número a dividir): "))
    divisor = int(input("Ingrese el divisor (número por el cual dividir): "))
    resto = resto_recursivo(dividendo, divisor)
    print(f"El resto de {dividendo} % {divisor} es: {resto}")
    
if __name__ == "__main__":
    main()  