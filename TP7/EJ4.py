def producto_recursivo(a, b):
    """
    Calcula a * b sumando 'a', 'b' veces.
    Pre: a y b son números enteros no negativos.
    Post: Devuelve el producto de a y b.
    """
    if b == 0:
        return 0
    
    # Paso Recursivo: Sumamos 'a' una vez y llamamos a la función
    # para que sume el resto (b - 1 veces)
    return a + producto_recursivo(a, b - 1)

def main():
    """
    Pregunta al usuario por dos números enteros y muestra su producto.
    Pre: El usuario debe ingresar dos números enteros no negativos.
    Post: Muestra el producto de los dos números ingresados.
    """
    a = int(input("Ingrese el primer número (a): "))
    b = int(input("Ingrese el segundo número (b): "))
    resultado = producto_recursivo(a, b)
    print(f"El producto de {a} y {b} es: {resultado}")

if __name__ == "__main__":
    main()