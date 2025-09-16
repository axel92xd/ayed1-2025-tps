import random as rn

def generar_peso_naranja() -> int:
    """
    Genera un peso aleatorio para una naranja entre 150 y 350 g.
    Pre: ninguna
    Post: devuelve un entero entre 150 y 350.
    """
    peso = rn.randint(150, 350)
    assert 150 <= peso <= 350
    return peso


def clasificar_naranjas(cantidad: int):
    """
    Clasifica las naranjas en aptas y para jugo según su peso.
    Pre: cantidad > 0
    Post: devuelve (lista_naranjas_validas, cantidad_jugo)
    """
    assert isinstance(cantidad, int) and cantidad > 0, "Cantidad inválida"

    validas = []
    jugo = 0
    cosecha = [generar_peso_naranja() for _ in range(cantidad)]  # lista de todas las naranjas
    
    for peso in cosecha:  
        if 200 <= peso <= 300:
            validas.append(peso)
        else:
            jugo += 1
    return validas, jugo


def llenar_cajones(naranjas: list):
    """
    Forma cajones de 100 naranjas válidas.
    Pre: naranjas es una lista de enteros (gramos).
    Post: devuelve (lista_cajones, sobrantes)
    """
    assert all(isinstance(p, int) and p > 0 for p in naranjas)

    cajones = []
    while len(naranjas) >= 100:
        cajon = naranjas[:100]
        cajones.append(cajon)
        naranjas = naranjas[100:]
    sobrantes = len(naranjas)
    return cajones, sobrantes


def cargar_camiones(cajones: list):
    """
    Carga cajones en camiones de hasta 500 kg.
    Cada camión debe estar cargado al menos al 80% (400 kg) para despacharse.
    Pre: cajones es lista de listas de pesos de naranjas.
    Post: devuelve el número de camiones despachados.
    """
    assert all(isinstance(c, list) for c in cajones)

    camiones = 0
    peso_actual = 0

    for cajon in cajones:  
        peso_cajon = sum(cajon)
        if peso_actual + peso_cajon <= 500000:
            peso_actual += peso_cajon
        else:
            if peso_actual >= 400000:
                camiones += 1
            peso_actual = peso_cajon
    
    if peso_actual >= 400000:
        camiones += 1

    return camiones


def main():
    cantidad = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    
    validas, jugo = clasificar_naranjas(cantidad)
    
    cajones, sobrantes = llenar_cajones(validas)
    
    camiones = cargar_camiones(cajones)

    print(f"Naranjas para jugo: {jugo}")
    print(f"Cajones completos: {len(cajones)}")
    print(f"Naranjas sobrantes (no completan cajón): {sobrantes}")
    print(f"Camiones despachados: {camiones}")


# Programa principal
main()
