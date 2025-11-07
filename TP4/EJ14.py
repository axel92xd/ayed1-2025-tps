def es_email_valido(email: str) -> bool:
    """
    
    Verifica si un email cumple con las 4 reglas del ejercicio.
    
    1. Usuario solo alfanumérico.
    2. Un solo '@'.
    3. Dominio con al menos un carácter (antes del sufijo).
    4. Termina en .com o .com.ar
    Pre: recibe como parámetro una cadena (email).
    Post: Retorna True si el email es válido, False en caso contrario.
    """
    
    # Verificar que haya un solo '@'
    if email.count('@') != 1:
        return False
        
    # Separamos el email en las dos partes
    try:
        usuario, dominio_completo = email.split('@')
    except ValueError:
        return False # Si split falla (ej: solo "@")

    # Verificar el usuario
    # comprueba si todos los caracteres son letras o números.
    if not usuario or not usuario.isalnum():
        return False
        
    # Verificar la terminación del dominio (ignorando mayúsculas/minúsculas)
    dominio_lower = dominio_completo.lower()
    
    # primero verificamos ".com.ar" porque si no, 
    # "mail@dominio.com.ar" sería leído como ".com" y fallaría.
    
    if dominio_lower.endswith('.com.ar'):
        # 3. Verificar que haya un nombre de dominio antes del sufijo
        # (Ej: previene que "@.com.ar" sea válido)
        parte_principal_dominio = dominio_lower[:-len('.com.ar')] # Saca el '.com.ar'
        
        if not parte_principal_dominio:
            return False
            
    elif dominio_lower.endswith('.com'):
        # 3. Verificar que haya un nombre de dominio antes del sufijo
        parte_principal_dominio = dominio_lower[:-len('.com')] # Saca el '.com'
        
        if not parte_principal_dominio:
            return False
            
    else:
        # Si no termina ni en .com ni en .com.ar
        return False
        
    # Si pasó todas las validaciones, es válido
    return True

def procesar_emails():
    """
    Función principal que pide emails, los valida y 
    almacena los dominios únicos.
    Pre: No recibe parámetros.
    Post: Muestra los dominios únicos al finalizar la entrada de datos.
    """
    
    # Usamos un 'set' (conjunto) para guardar los dominios.
    # Un 'set' automáticamente ignora los duplicados.
    dominios_unicos = set()
    
    print("Ingrese direcciones de correo (presione Enter con el campo vacío para terminar):")
    
    while True:
        email_ingresado = input("Correo: ").strip() # .strip() saca espacios en blanco
        
        # Condición de salida: cadena vacía
        if not email_ingresado:
            break
            
        if es_email_valido(email_ingresado):
            print("Válido")
            
            # Extraemos el dominio (la parte después del @)
            dominio = email_ingresado.split('@')[1]
            
            # Lo agregamos al set en minúsculas
            dominios_unicos.add(dominio.lower())
            
        else:
            print("Inválido")

    
    if not dominios_unicos:
        print("\nNo se ingresaron correos válidos.")
        return

    
    lista_dominios = list(dominios_unicos)
    
    # 2. Ordenamos la lista alfabéticamente
    lista_dominios.sort()
    
    print("\n--- Dominios Únicos (ordenados) ---")
    for dominio in lista_dominios:
        print(f"- {dominio}")

def main():
    """
    Función principal del programa.
    Pre: No recibe parámetros.
    Post: Ejecuta la función para procesar emails.
    """
    procesar_emails()
    
if __name__== "__main__":
    main()