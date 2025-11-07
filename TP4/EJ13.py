
unidades = [
    'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'
]

# Casos especiales del 10 al 29
decenas = [
    'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis',
    'diecisiete', 'dieciocho', 'diecinueve', 'veinte', 'veintiuno',
    'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis',
    'veintisiete', 'veintiocho', 'veintinueve'
]

# Decenas regulares (30, 40, ...)
decenas_base = [
    '', '', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'
]

# Centenas (Notar "ciento" para 101-199 y "cien" para 100)
centenas = [
    '', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos',
    'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos'
]

def convertir_tres_cifras(n: int) -> str:
    """
    Función ayudante. Convierte un número de tres cifras (0-999) a su representación en letras.
    Pre: n es un entero entre 0 y 999.
    Post: Retorna el número en letras.
    """
    
    # --- Caso especial "cien" ---
    if n == 100:
        return "cien"
    
    # --- Centenas ---
    partes = []
    centena = n // 100
    resto = n % 100
    
    if centena > 0:
        partes.append(centenas[centena])

    # --- Decenas y Unidades ---
    if resto > 0:
        if resto < 10:
            # Caso 0-9
            partes.append(unidades[resto])
        elif resto < 30:
            # Caso 10-29 (usa las listas especiales)
            partes.append(decenas[resto - 10])
        else:
            # Caso 30-99 (ej: "ochenta y nueve")
            decena_str = decenas_base[resto // 10]
            unidad = resto % 10
            
            if unidad == 0:
                partes.append(decena_str)
            else:
                # Ej: 89 ("ochenta y nueve")
                partes.append(f"{decena_str} y {unidades[unidad]}")
                
    return " ".join(partes)

def en_letras(numero: int) -> str:
    """
    Convierte un entero (hasta 1 Billón) a letras usando una función ayudante.
    Pre: recibe como parametro un entero positivo
    Post: Retorna el numero en letras.
    """
    
    if numero == 0:
        return "cero"
    
    if numero > 1_000_000_000_000:
        return "Error: Número demasiado grande."

    if numero == 1_000_000_000_000:
        return "un billón"
        
    
    unidades = numero % 1000
    miles = (numero // 1000) % 1000
    millones = (numero // 1_000_000) % 1000
    miles_de_millones = (numero // 1_000_000_000) % 1000
    billones = (numero // 1_000_000_000_000) % 1000
    
    partes_texto = []

    # 2. Convertimos cada grupo (de mayor a menor)
    
    if billones > 0:
        if billones == 1:
            partes_texto.append("un billón")
        else:
            partes_texto.append(f"{convertir_tres_cifras(billones)} billones")
    
    if miles_de_millones > 0:
        if miles_de_millones == 1:
             partes_texto.append("mil millones")
        else:
            partes_texto.append(f"{convertir_tres_cifras(miles_de_millones)} mil millones")
            
    if millones > 0:
        if millones == 1:
            partes_texto.append("un millón")
        else:
            partes_texto.append(f"{convertir_tres_cifras(millones)} millones")

    if miles > 0:
        #Caso especial para mil
        if miles == 1:
            partes_texto.append("mil")
        else:
            partes_texto.append(f"{convertir_tres_cifras(miles)} mil")

    if unidades > 0:
        partes_texto.append(convertir_tres_cifras(unidades))
        
    return " ".join(partes_texto)

def main() -> None:
    """
    Se ingresa un numero entero y se invoca la funcion en_letras para convertir
    ese numero en letras.
    Pre: El usuario ingresa un numero entero positivo.
    Post: Se imprime el numero en letras.
    """
    try:
        numero = int(input("Ingrese un numero (0 a 1 billón): "))
        if numero < 0:
             print("Debe ser un numero positivo.")
        else:
             print(f"\nEn letras: {en_letras(numero)}")
             
             # Pruebas de los casos que fallaban antes:
             print("\n--- Casos de prueba ---")
             print(f"101: {en_letras(101)}")
             print(f"31: {en_letras(31)}")
             print(f"1001: {en_letras(1001)}")
             print(f"1000000: {en_letras(1000000)}")
             print(f"1234567: {en_letras(1234567)}")
             
    except ValueError:
        print("Error: Debe ser un numero entero.")

main()