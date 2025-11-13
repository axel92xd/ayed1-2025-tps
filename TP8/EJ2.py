# Lista (o Tupla) de meses
meses = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

anio_corte = 30

def fecha_a_texto_extendido(fecha_tupla: tuple) -> str:
    """
    Convierte una tupla (dia, mes, año) a un string en formato extendido.
    Maneja el "año de corte" para años de 2 dígitos.
    
    Pre:  fecha_tupla (dia, mes, anio) - ej: (25, 12, 31)
    Post: Devuelve un string (ej: "25 de Diciembre de 1931")
    """
    
    try:
        dia, mes, anio = fecha_tupla
        
        # Validar Día y Mes
        if not (1 <= dia <= 31):
            return "Error: Día inválido."
        if not (1 <= mes <= 12):
            return "Error: Mes inválido."
            
        nombre_mes = meses[mes - 1] # (mes 1 = índice 0)
        
        # Lógica del Año de Corte
        
        if 0 <= anio <= 99:
            # Es un año de 2 dígitos
            if anio <= anio_corte:
                # ej: 30 -> 2030
                anio_final = 2000 + anio
            else:
                # ej: 31 -> 1931
                anio_final = 1900 + anio
        elif anio > 99:
            # Es un año de 4 dígitos, no usamos el corte
            anio_final = anio
        else:
            return "Error: Año negativo."
            
        # Formatear el string de salida
        return f"{dia} de {nombre_mes} de {anio_final}"

    except IndexError:
        return "Error: Mes fuera de rango."
    except Exception as e:
        return f"Error inesperado: {e}"

if __name__ == "__main__":
    
    try:
        dia_in = int(input("Ingrese día: "))
        mes_in = int(input("Ingrese mes: "))
        anio_in = int(input("Ingrese año (2 o 4 dígitos): "))
        
        fecha_ingresada = (dia_in, mes_in, anio_in)
        
        resultado = fecha_a_texto_extendido(fecha_ingresada)
        print(f"Resultado: {resultado}")
        
        print("\n--- Pruebas de ejemplo ---")
        print(f"(12, 10, 30) -> {fecha_a_texto_extendido( (12, 10, 30) )}")
        print(f"(25, 12, 31) -> {fecha_a_texto_extendido( (25, 12, 31) )}")
        print(f"(15, 5, 2024) -> {fecha_a_texto_extendido( (15, 5, 2024) )}")
        
    except ValueError:
        print("Error: Día, mes y año deben ser números enteros.")   