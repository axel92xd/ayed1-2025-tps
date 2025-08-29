def vuelto (total: int, recibido: int) -> list:
    """
    Calcula la cantidad de billetes que se debe devolver segun un pago.
    Pre: Total y Recibido son valores enteros que recibe la funcion
    Post: Devuelve los valores de una lista que representan la cantidad de billetes
    """
    # Validar precondiciones
    assert isinstance(recibido, int) and recibido > 0, f"{recibido} debe ser un entero positivo"
    assert isinstance(total, int) and total > 0, f"{total} debe ser un entero positivo"
    assert isinstance(recibido, int) and recibido > total, f"{recibido} debe ser mayor a {total}"
    

        
    if total > recibido:
        return[-1]
    #Crea una lista de 7 elementos de 0
    billetes = []
    #Calcula lo que debe devolver
    devolver = recibido - total
    for v in valores:
        billetes.append(devolver//v)
        devolver %= v
    return billetes

valores = [5000,1000,500,100,50,10]     
def main():
    pago = int(input("Ingrese el total de la compra: "))
    billete = int(input("Ingrese el monto a pagar: "))
    
    if pago > billete:
        print("No alcanza para hacer el pago")
    else:
        salida = vuelto(pago,billete)
        for i,s in enumerate(salida):
            if s: # Si "s" es 0 lo considera falso y no sigue con la siguiente linea, si llega a ser cualquier valor diferente a 0 va a seguir con el codigo
                print(f"{s} billetes de {valores[i]}")

if __name__ == "__main__":
    main()
    
    
    