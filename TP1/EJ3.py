
def calcular_gasto_subte(viajes: int) -> float:
    """
    Calcula el total gastado en viajes en subte según la cantidad de viajes realizados.

    Pre: viajes es un entero positivo que representa la cantidad de viajes realizados en el mes.
    Post: Devuelve el total gastado en pesos, aplicando las tarifas decrecientes correspondientes.
    """
    assert isinstance(viajes, int) and viajes > 0, "La cantidad de viajes debe ser un número entero positivo"
    
    tarifa_base = 1031.00
    total = 0.0

    # Generar lista de viajes sin usar range
    lista_viajes = []
    contador = 1
    while contador <= viajes:
        lista_viajes.append(contador)
        contador += 1

    # Calcular tarifas
    for viaje in lista_viajes:
        if viaje <= 20:
            tarifa = tarifa_base
        elif viaje <= 30:
            tarifa = tarifa_base * 0.8   # 20% descuento
        elif viaje <= 40:
            tarifa = tarifa_base * 0.7   # 30% descuento
        else:
            tarifa = tarifa_base * 0.6   # 40% descuento
        total += tarifa

    assert total >= 0
    return total


def main():
    viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
    total = calcular_gasto_subte(viajes)
    print(f"Total gastado en subte: ${total:,.2f}")

if __name__ == "__main__":
    main()
