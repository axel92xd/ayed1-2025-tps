def email_a_tupla(email: str) -> tuple:
    """
    Convierte un string de email en una tupla de sus partes.
    
    Pre:  Un string de email (ej: "alguien@uade.edu.ar")
    Post: Una tupla (ej: ('alguien', 'uade', 'edu', 'ar')) o una tupla vacía si el formato es inválido.
    """
    
    email = email.strip() # Limpiamos espacios
    
    # Validar que haya un solo '@'
    if email.count('@') != 1:
        return () # Tupla vacía si hay 0 o más de 1 arroba
        
    # Separamos usuario y dominio
    try:
        usuario, dominio_completo = email.split('@')
    except ValueError:
        return () # Si falla (ej: solo "@")

    # Validar que no estén vacíos
    if not usuario or not dominio_completo:
        return () # ej: "@uade.com" o "alguien@"

    # Validar que el dominio tenga al menos un punto
    if '.' not in dominio_completo:
        return () # ej: "alguien@servidor"

    # Separamos el dominio por los puntos
    partes_dominio = dominio_completo.split('.')
    
    # Validar que no haya partes vacías
    #    (ej: "alguien@uade..ar" -> split da ['uade', '', 'ar'])
    for parte in partes_dominio:
        if not parte:
            return () # Tupla vacía

    # Creamos la lista final y la convertimos en tupla
    lista_final = [usuario] + partes_dominio
    return tuple(lista_final)

if __name__ == "__main__":
    
    
    ejemplos = [
        "alguien@uade.edu.ar",
        "usuario.valido@gmail.com",
        "invalido@sinpunto",
        "invalido.com",
        "muchos@@arrobas.com",
        "@vacio.com",
        "usuario@.com" 
    ]
    
    for email in ejemplos:
        resultado = email_a_tupla(email)
        print(f"'{email}' -> {resultado}")