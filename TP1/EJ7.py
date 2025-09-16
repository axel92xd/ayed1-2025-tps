def diasiguiente(dia:int, mes:int, año:int):
    """
    Calcula el día siguiente de la fecha ingresada.
    pre: dia, mes, año son enteros positivos, y forman una fecha válida.
    post: devuelve tres enteros: dia, mes, año del día siguiente.
    """
    assert isinstance(dia,int) and dia > 0, f"{dia} debe ser un entero positivo"
    assert isinstance(mes,int) and 1 <= mes <= 12, f"{mes} debe estar entre 1 y 12"
    assert isinstance(año,int) and año > 0, f"{año} debe ser un entero positivo"
    
    # Meses con 31 días
    mes_31 = [1,3,5,7,8,10,12]
    mes_30 = [4,6,9,11]
    if mes in mes_31:
        if dia < 31:
            dia += 1
        else:
            dia = 1
            if mes == 12:
                mes = 1
                año += 1
            else:
                mes += 1
    # Meses con 30 días
    elif mes in mes_30:
        assert dia <= 30, f"{dia} es inválido para el mes {mes}"
        if dia < 30:
            dia += 1
        else:
            dia = 1
            mes += 1
    # Febrero
    else:
        bisiesto = año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
        if bisiesto:
            assert dia <= 29, f"{dia} es inválido para febrero en año bisiesto"
            if dia < 29:
                dia += 1
            else:
                dia = 1
                mes = 3
        else:
            assert dia <= 28, f"{dia} es inválido para febrero en año no bisiesto"
            if dia < 28:
                dia += 1
            else:
                dia = 1
                mes = 3
    return dia, mes, año


def sumar_dias(dia:int, mes:int, año:int, num:int):
    """
    Suma N días a la fecha ingresada usando diasiguiente.
    pre: N es entero positivo
    post: devuelve la fecha resultante como 3 enteros
    """
    assert isinstance(num,int) and num >= 0, "N debe ser un entero positivo"

    for i in range(num):
        dia, mes, año = diasiguiente(dia, mes, año)
    return dia, mes, año


def dias_entre_fechas(dia1:int, mes1:int, año1:int, dia2:int, mes2:int, año2:int):
    """
    Calcula la cantidad de días entre dos fechas
    pre: la segunda fecha es mayor o igual a la primera
    post: devuelve un entero
    """
    # Validar que la segunda fecha sea mayor o igual
    assert (año2, mes2, dia2) >= (año1, mes1, dia1), "La segunda fecha debe ser posterior o igual a la primera"
    
    contador = 0
    while (dia1, mes1, año1) != (dia2, mes2, año2):
        dia1, mes1, año1 = diasiguiente(dia1, mes1, año1)
        contador += 1
    return contador


# Programa principal
def main():
    print("Ingrese la fecha inicial:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))

    # Día siguiente
    d, m, a = diasiguiente(dia, mes, año)
    print(f"Día siguiente: {d}/{m}/{a}")

    # Sumar N días
    N = int(input("Ingrese N días a sumar: "))
    d2, m2, a2 = sumar_N_dias(dia, mes, año, N)
    print(f"Fecha luego de sumar {N} días: {d2}/{m2}/{a2}")

    # Diferencia entre fechas
    print("Ingrese la segunda fecha:")
    dia2 = int(input("Día: "))
    mes2 = int(input("Mes: "))
    año2 = int(input("Año: "))
    total = dias_entre_fechas(dia, mes, año, dia2, mes2, año2)
    print(f"Días entre las fechas: {total}")

main()
