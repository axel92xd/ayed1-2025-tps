# Definimos los nombres de los archivos
archivo_entrada = "programa_con_comentarios.py"
archivo_salida = "programa_limpio.py"

def limpiar_comentarios_simple(archivo_entrada, archivo_salida):
    """
    Intenta eliminar comentarios y docstrings de un archivo Python
    de una manera simple.
    
    Pre:  Recibe el nombre del archivo de entrada y el de salida.
    Post: Crea un archivo de salida sin comentarios.
    """
    
    try:
        # Abrimos ambos archivos
        with open(archivo_entrada, 'rt', encoding='utf-8') as file_entrada, \
             open(archivo_salida, 'wt', encoding='utf-8') as file_salida:
            
            for linea_original in file_entrada: # linea_original incluye el '\n'
                
                # --- 1. Lógica simple para Docstrings ---
                # Quitamos espacios al inicio/final SÓLO para chequear
                linea_chequeo = linea_original.strip()
                
                # Si la línea empieza con comillas de docstring, la saltamos
                if linea_chequeo.startswith("'''") or linea_chequeo.startswith('"""'):
                    continue # Saltamos esta línea

                # --- 2. Lógica simple para Comentarios (#) ---
                
                # Buscamos la posición del primer '#'
                posicion_hash = linea_original.find('#')
                
                # Si se encontró un '#' (find() devuelve -1 si no lo encuentra)
                if posicion_hash != -1:
                    # Cortamos la línea: desde el inicio HASTA el '#'
                    linea_final = linea_original[:posicion_hash]
                else:
                    # Si no hay '#', la línea está limpia (solo quitamos el \n)
                    linea_final = linea_original.rstrip('\n')
                
                # 3. Escribir (solo si la línea no quedó vacía)
                if linea_final.strip(): # Chequeamos si quedó algo
                    file_salida.write(linea_final + '\n') # Escribimos y agregamos un \n limpio

        print(f"Archivo '{archivo_salida}' creado con éxito.")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Programa Principal ---
if __name__ == "__main__":
    
    # --- 1. Crear un archivo de ejemplo para probar ---
    # (Este archivo SÍ tiene # en los strings para que veas el fallo)
    print(f"Creando archivo de ejemplo '{archivo_entrada}'...")
    try:
        with open(archivo_entrada, "wt", encoding='utf-8') as file_entrada:
            file_entrada.write("# Esto es un comentario de línea completa\n")
            file_entrada.write("\n")
            file_entrada.write("def mi_funcion(a, b):\n")
            file_entrada.write("    '''Esto es un docstring (será eliminado)'''\n")
            file_entrada.write("    resultado = a + b # Esto es un comentario (será eliminado)\n")
            file_entrada.write('    color_hash = "#FF0000" # Este es el error de la lógica simple\n')
            file_entrada.write("    return resultado\n")
        
        # 2. Ejecutar la función de limpieza
        limpiar_comentarios_simple(archivo_entrada, archivo_salida)
        
        print(f"\nRevisar '{archivo_salida}' para ver el resultado.")
        
    except Exception as e:
        print(f"Error creando el archivo de ejemplo: {e}")