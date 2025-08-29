def calcular_gasto_subte(viajes: int) -> float:
    """
    Calcula el total gastado en viajes en subte según la cantidad de viajes realizados.

    Pre: viajes es un entero positivo que representa la cantidad de viajes realizados en el mes.
    Post: Devuelve el total gastado en pesos, aplicando las tarifas decrecientes correspondientes.
    """
    assert isinstance(viajes, int) and viajes > 0, "La cantidad de viajes debe ser un número entero positivo"
    
    # Tarifas por rango de viajes
    """
    Calcula el total gastado en el subte según la cantidad de viajes,
    aplicando automáticamente los descuentos según la tabla.
    """
    total = 0
    tarifa_base = 1031.00
    
    for i in range(1, viajes + 1):
        if i <= 20:
            tarifa = tarifa_base
        elif i <= 30:
            tarifa = tarifa_base * 0.8   # 20% descuento
        elif i <= 40:
            tarifa = tarifa_base * 0.7   # 30% descuento
        else:
            tarifa = tarifa_base * 0.6   # 40% descuento
        total += tarifa

    return total
def main():
    viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
    total = calcular_gasto_subte(viajes)
    print(f"Total gastado en subte: ${total:,.2f}")

if __name__ == "__main__":
    main()

