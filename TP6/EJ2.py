def dividir_archivo(nombre_archivo: str, tamano_max_bytes: int):
    """
    Divide un archivo de texto en múltiples partes sin cargar todo en memoria
    y sin cortar líneas.

    Pre:  Recibe el nombre del archivo a dividir y el tamaño máximo
          en bytes que debe tener cada parte.
    Post: Crea uno o más archivos conteniendo los datos divididos.
    """
    
    f_salida = None # Variable para el archivo de salida 
    
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8-sig') as f_entrada:
            
            numero_parte = 1
            tamano_actual_bytes = 0
            
            # Buscamos la posición del ÚLTIMO punto
            pos_punto = nombre_archivo.rfind('.')
            if pos_punto == -1:
                # Si no hay extensión (ej: 'miarchivo')
                nombre_base, extension = nombre_archivo, ""
            else:
                # Si hay extensión (ej: 'mi.archivo.txt')
                nombre_base, extension = nombre_archivo[:pos_punto], nombre_archivo[pos_punto:]
            # --- Fin lógica nombre ---
            
            # Abrimos el PRIMER archivo de salida (para escribir)
            nombre_salida = f"{nombre_base}_parte_{numero_parte}{extension}"
            f_salida = open(nombre_salida, 'wt', encoding='utf-8')
            print(f"Creando parte {numero_parte}: '{nombre_salida}'...")
            
            for linea in f_entrada:
                
                # Medimos los bytes de la línea (no los caracteres)
                try:
                    linea_bytes = len(linea.encode('utf-8'))
                except UnicodeEncodeError:
                     print("Ignorando línea con caracter inválido...")
                     continue

                if linea_bytes > tamano_max_bytes:
                    print(f"Error: Una línea ({linea_bytes} bytes) es más grande que el límite ({tamano_max_bytes} bytes).")
                    print("Proceso terminado.")
                    return

                # Lógica de corte: Si la línea no entra en el archivo actual
                if (tamano_actual_bytes + linea_bytes) > tamano_max_bytes and tamano_actual_bytes > 0:
                    
                    # Cerramos el archivo viejo
                    f_salida.close()
                    
                    # Preparamos el nuevo
                    numero_parte += 1
                    tamano_actual_bytes = 0 # Reseteamos el contador
                    
                    nombre_salida = f"{nombre_base}_parte_{numero_parte}{extension}"
                    f_salida = open(nombre_salida, 'wt', encoding='utf-8')
                    print(f"Creando parte {numero_parte}: '{nombre_salida}'...")

                f_salida.write(linea)
                tamano_actual_bytes += linea_bytes

            print(f"\n¡División de archivo completada en {numero_parte} parte(s)!")

    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{nombre_archivo}' no se encontró.")
    finally:
        if f_salida and not f_salida.closed:
            f_salida.close()
            print("Archivo final cerrado.")

if __name__ == "__main__":
    
    nombre_archivo_original = input("Ingrese el nombre del archivo que desea dividir: ")
    
    try:
        tamano_str = input("Ingrese el tamaño máximo por parte (en bytes, ej: 100): ")
        tamano_maximo = int(tamano_str)
        
        if tamano_maximo <= 0:
             print("Error: El tamaño debe ser un número positivo.")
        else:
            dividir_archivo(nombre_archivo_original, tamano_maximo)
            
    except ValueError:
        print("Error: El tamaño debe ser un número entero.")