from typing import List, Dict

# ==================== Funciones ====================

def cargar_socios() -> List[int]:
    """
    Carga los números de socio hasta ingresar 0.
    
    Pre: Número de socio entero de 5 dígitos o 0
    Post: Lista de números de socio en orden de ingreso
    """
    socios = []
    while True:
        nro = int(input("Ingrese número de socio (5 dígitos, 0 para terminar): "))
        if nro == 0:
            break
        socios.append(nro)
    return socios

def contar_ingresos(socios: List[int]) -> Dict[int, int]:
    """
    Cuenta cuántas veces ingresó cada socio.
    
    Pre: lista de socios
    Post: diccionario {socio: cantidad de ingresos}
    """
    conteo = {}
    for socio in socios:
        conteo[socio] = conteo.get(socio, 0) + 1
    return conteo

def eliminar_socio(socios: List[int], nro: int) -> int:
    """
    Elimina todos los ingresos de un socio dado.
    
    Pre: lista de socios, nro a eliminar
    Post: devuelve cantidad de ingresos eliminados
    """
    original_len = len(socios)
    socios[:] = [i for i in socios if i != nro]
    return original_len - len(socios)

def main():
    socios = cargar_socios()
    print("\nRegistros de ingreso:", socios)
    
    conteo = contar_ingresos(socios)
    print("\nCantidad de ingresos por socio:")
    for socio, cant in conteo.items():
        print(f"Socio {socio}: {cant} ingreso(s)")
    
    nro_eliminar = int(input("\nIngrese número de socio a eliminar: "))
    eliminados = eliminar_socio(socios, nro_eliminar)
    
    print("\nRegistros después de eliminar:", socios)
    print(f"Se eliminaron {eliminados} ingreso(s) del socio {nro_eliminar}")

if __name__ == "__main__":
    main()