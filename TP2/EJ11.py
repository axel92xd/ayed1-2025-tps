from typing import List, Tuple

def cargar_pacientes() -> Tuple[List[int], List[int]]:
    """
    Carga los pacientes hasta ingresar -1 como número de afiliado.
    Separa los pacientes por urgencia (0) y turno (1).
    
    Pre: El numero de afiliado es entero de 4 dígitos y el tipo 0 o 1
    Post: Devuelve dos listas: urgencia y turno, con los números de afiliado en orden de llegada
    """
    urgencia = []
    turno = []
    
    while True:
        nro_afiliado = int(input("Ingrese numero de afiliado (4 dígitos, -1 para terminar): "))
        if nro_afiliado == -1:
            break
        tipo = int(input("Ingrese 0 para urgencia, 1 para turno: "))
        assert tipo in [0, 1], "El tipo debe ser 0 o 1"
        if tipo == 0:
            urgencia.append(nro_afiliado)
        else:
            turno.append(nro_afiliado)
    return urgencia, turno

def buscar_afiliado(nro: int, urgencia: List[int], turno: List[int]) -> Tuple[int, int]:
    """
    Cuenta cuantas veces un afiliado fue atendido por urgencia y por turno.
    
    Pre: nro >= 0
    Post: Devuelve dos enteros: cantidad urgencias y cantidad turnos
    """
    return urgencia.count(nro), turno.count(nro)

def main():
    urgencia, turno = cargar_pacientes()
    
    print("\nPacientes atendidos por urgencia:", urgencia)
    print("Pacientes atendidos por turno:", turno)
    
    while True:
        nro_buscar = int(input("\nIngrese número de afiliado a buscar (-1 para terminar): "))
        if nro_buscar == -1:
            break
        urgencia, turno = buscar_afiliado(nro_buscar, urgencia, turno)
        print(f"Atendido por urgencia: {urgencia} veces, por turno: {turno} veces")

if __name__ == "__main__":
    main()
