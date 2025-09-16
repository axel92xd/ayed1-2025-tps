def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha dada (día, mes, año) es válida.
    Pre: dia, mes, anio son enteros positivos
    Post: Devuelve True si la fecha es válida, False en caso contrario
    """
    # Validar precondiciones
    assert isinstance(dia, int) and dia > 0, f"{dia} debe ser un entero positivo"
    assert isinstance(mes, int) and mes > 0, f"{mes} debe ser un entero positivo"
    assert isinstance(anio, int) and anio > 0, f"{anio} debe ser un entero positivo"

    # Meses con 31 días
    for i in [1, 3, 5, 7, 8, 10, 12]:
        if mes == i:
            return dia <= 31

    # Meses con 30 días
    for i in [4, 6, 9, 11]:
        if mes == i:
            return dia <= 30

    # Febrero
    if mes == 2:
        # Verificar si es bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return dia <= 29
        else:
            return dia <= 28

    # Mes inválido
    return False


# Programa de prueba
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha NO es válida.")
