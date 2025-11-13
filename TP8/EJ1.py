def pedir_entero(texto_prompt: str) -> int:
    """
    Pide un entero al usuario y valida que sea un número.
    
    Pre: Recibe un string con el texto a mostrar (ej: "el día").
    Post: Retorna el entero validado.
    """
    while True:
        valor_str = input(f"Ingrese {texto_prompt}: ")
        try:
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(f"Error: El valor para '{texto_prompt}' debe ser un número entero.")


def es_bisiesto(anio: int) -> bool:
    """
    Calcula si el año ingresado es bisiesto o no (lógica completa).

    Pre: El año debe ser un entero positivo.
    Post: Devuelve True si es bisiesto, False si no.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes: int, anio: int) -> int:
    """
    Devuelve cuántos días tiene un mes específico,
    considerando si el año es bisiesto (para Febrero).
    Pre:  mes (1-12), anio (entero positivo)
    Post: Retorna la cantidad de días del mes (int).
    """
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    else:
        return -1 # Mes inválido

def ingresar_fecha_valida() -> tuple:
    """
    Pide una fecha (día, mes, año) y la valida manualmente.
    
    Pre: No recibe parámetros.
    Post: Retorna una tupla (dia, mes, anio) validada.
    """
    print("--- Ingrese una Fecha ---")
    while True:
        dia = pedir_entero("el día (DD)")
        mes = pedir_entero("el mes (MM)")
        anio = pedir_entero("el año (AAAA)")
        
        # Validamos los rangos
        max_dias = dias_en_mes(mes, anio)
        
        if max_dias == -1: # Mes inválido
            print(f"Error: El mes {mes} no existe.")
        elif not (1 <= dia <= max_dias):
            print(f"Error: El día {dia} es inválido para ese mes/año (debe ser 1-{max_dias}).")
        elif anio <= 0:
             print("Error: El año debe ser positivo.")
        else:
            print("Fecha válida registrada.")
            return (dia, mes, anio) # Fecha correcta, salimos

def sumar_n_dias(fecha_tupla: tuple, dias_a_sumar: int) -> tuple:
    """
    Suma N días a una fecha (recibida como tupla)
    
    Pre:  fecha_tupla (dia, mes, anio), dias_a_sumar (int >= 0)
    Post: Devuelve una nueva tupla (dia, mes, anio) con la fecha resultante.
    """
    dia, mes, anio = fecha_tupla
    
    for _ in range(dias_a_sumar):
        
        max_dias_mes_actual = dias_en_mes(mes, anio)
        
        dia += 1
        
        # Chequeamos si pasamos al mes siguiente
        if dia > max_dias_mes_actual:
            dia = 1
            mes += 1
            
            # Chequeamos si pasamos al año siguiente
            if mes > 12:
                mes = 1
                anio += 1
    
    return (dia, mes, anio)

def ingresar_horario_valido() -> tuple:
    """
    Pide al usuario un horario (hh, mm) y lo valida
    manualmente.
    
    Pre:  No recibe parámetros.
    Post: Devuelve una tupla (hora, minuto) validada.
    """
    print("--- Ingrese un Horario ---")
    while True:
        hora = pedir_entero("la hora (0-23)")
        minuto = pedir_entero("los minutos (0-59)")

        if not (0 <= hora <= 23):
            print("Error: La hora debe estar entre 0 y 23.")
        elif not (0 <= minuto <= 59):
            print("Error: Los minutos deben estar entre 0 y 59.")
        else:
            print("Horario válido registrado.")
            return (hora, minuto)

def calcular_diferencia_de_horario(horario1: tuple, horario2: tuple) -> tuple:
    """
    Verifica la diferencia entre 2 horarios (tuplas de h, m).
    Usa la lógica de contador simple del 
    
    Pre: Recibe dos tuplas (hora, minuto).
    Post: Retorna (horas_dif, minutos_dif) de diferencia.
    """
    
    contador_minutos = 0
    
    # Creamos una copia mutable (una lista) para poder iterar
    h_actual, m_actual = horario1
    
    # Iteramos 1 minuto a la vez hasta alcanzar el horario 2
    # (Limitamos a 24*60 iteraciones para evitar bucles infinitos)
    while (h_actual, m_actual) != horario2:
        m_actual += 1
        
        if m_actual == 60:
            m_actual = 0
            h_actual += 1
            
        if h_actual == 24:
            h_actual = 0
        
        contador_minutos += 1
        
        # Regla: "En ningún caso la diferencia puede superar las 24 horas"
        if contador_minutos > (24 * 60):
            print("Error: La diferencia supera las 24h (bucle infinito).")
            return (0, 0) # Devolvemos 0

    # Convertimos los minutos totales a Horas y Minutos
    horas_dif = contador_minutos // 60
    minutos_dif = contador_minutos % 60
    
    return (horas_dif, minutos_dif)

def main():
    """
    Menú principal que vincula todas las funciones.
    Pre: No recibe parámetros.
    Post: Ejecuta el programa completo.
    """
    
    fecha_principal = ingresar_fecha_valida()
    print(f"Fecha base guardada: {fecha_principal}")
    
    dias_str = input("\nIngrese cuántos días quiere sumar a la fecha: ")
    try:
        dias = int(dias_str)
        if dias < 0:
            print("No se pueden sumar días negativos.")
        else:
            nueva_fecha = sumar_n_dias(fecha_principal, dias)
            print(f"-> El resultado es: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")
    except ValueError:
        print("Error: Debe ingresar un número.")

    
    horario1 = ingresar_horario_valido()
    
    print("\nAhora, ingrese el segundo horario para calcular la diferencia.")
    horario2 = ingresar_horario_valido()
    
    
    horas, minutos = calcular_diferencia_de_horario(horario1, horario2)
    print(f"\nLa diferencia entre {horario1} y {horario2} es de: {horas} horas y {minutos} minutos.")
    
    print("\n--- Fin del Programa ---")

if __name__ == "__main__":
    main()