def diadelasemana(dia: int, mes: int, año: int) -> int:
    """
    Calcula el día de la semana para una fecha.
    pre: dia, mes, año forman una fecha válida.
         1 <= mes <= 12, año > 0
    post: devuelve un entero entre 0 y 6,
          donde 0=domingo, 1=lunes, ..., 6=sábado
    """
    assert isinstance(dia, int) and dia > 0, "El día debe ser un entero positivo"
    assert isinstance(mes, int) and 1 <= mes <= 12, "El mes debe estar entre 1 y 12"
    assert isinstance(año, int) and año > 0, "El año debe ser positivo"

    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    
    siglo = año // 100
    año2 = año % 100
    
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    
    if diasem < 0:
        diasem += 7

    assert 0 <= diasem <= 6, "El resultado debe estar entre 0 y 6"
    return diasem


def dias_en_mes(mes: int, año: int) -> int:
    """
    Devuelve la cantidad de días que tiene un mes en un año dado.
    pre: 1 <= mes <= 12, año > 0
    post: resultado en [28,29,30,31]
    """
    assert isinstance(mes, int) and 1 <= mes <= 12, "Mes inválido"
    assert isinstance(año, int) and año > 0, "Año inválido"

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes in [4, 6, 9, 11]:
        dias = 30
    else:  # Febrero
        bisiesto = año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
        dias = 29 if bisiesto else 28

    assert dias in [28, 29, 30, 31], "Número de días inválido"
    return dias


def imprimir_calendario(mes: int, año: int) -> None:
    """
    Imprime en pantalla el calendario de un mes y año dados.
    pre: 1 <= mes <= 12, año > 0
    post: imprime el calendario con formato correcto
    """
    assert isinstance(mes, int) and 1 <= mes <= 12, "Mes inválido"
    assert isinstance(año, int) and año > 0, "Año inválido"

    print(f"\n   Calendario {mes}/{año}")
    print("Do Lu Ma Mi Ju Vi Sa")
    
    # Día de la semana del 1 del mes
    inicio = diadelasemana(1, mes, año)
    dias = dias_en_mes(mes, año)
    
    # Espacios iniciales
    print("   " * inicio, end="")

    # Imprime días del mes
    for dia in range(1, dias + 1):
        print(f"{dia:2}", end=" ")
        inicio += 1
        if inicio % 7 == 0:  # salto de línea cada semana
            print()
    print("\n")


def main():
    """
    Programa principal.
    Permite al usuario ingresar mes y año, y muestra el calendario.
    """
    mes = int(input("Ingrese el mes (1-12): "))
    año = int(input("Ingrese el año: "))
    imprimir_calendario(mes, año)


# Programa principal
main()
