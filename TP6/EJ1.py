
paises_archivos = {
    'ian': 'ARMENIA.TXT',
    'ini': 'ITALIA.TXT',
    'ez': 'ESPAÑA.TXT',
}

# Nombre del archivo de entrada
archivo_entrada = 'nombres_entrada.txt' 


def guardar_apellido(apellido_comparar: str, linea_original: str):
    """
    Recibe un apellido y la línea original.
    Si el apellido coincide con el diccionario, abre el archivo
    correspondiente en modo 'at' (append/añadir) y guarda la línea.
    
    Pre:  apellido_comparar(str), linea_original (str)
    Post: Escribe en el archivo de salida si hay coincidencia.
    """
    
    # Recorremos el diccionario 
    for terminacion, archivo_destino in paises_archivos.items():
        
        if apellido_comparar.endswith(terminacion):
            try:
                with open(archivo_destino, 'at', encoding='utf-8') as f_salida:

                    f_salida.write(linea_original)
                    
                break 
                
            except IOError as e:
                print(f"Error al escribir en {archivo_destino}: {e}")
            except Exception as e:
                print(f"Error inesperado al escribir: {e}")

def main():
    """
    Programa principal. Lee el archivo de entrada línea por línea
    y llama a la función de clasificación.
    Pre:  archivo_entrada (str)
    Post: Crea archivos de salida con los apellidos clasificados.
    """
        
    try:
        # 4. Abrimos el archivo de entrada (con 'with' es más seguro)
        with open(archivo_entrada, 'rt', encoding='utf-8-sig') as f_entrada:
            
            # Leemos línea por línea
            for linea_original in f_entrada:
                
                # Limpiamos espacios en blanco o saltos de línea
                linea_limpia = linea_original.strip()
                
                if not linea_limpia: 
                    continue
                    
                try:
                    # Separamos y limpiamos el apellido
                    apellido = linea_limpia.split(',', 1)[0]
                    apellido_limpio = apellido.strip()
                    
                    if not apellido_limpio: # Si la línea es ", Nombre"
                        continue
                        
                    # 7. Llamamos a la función para clasificar
                    guardar_apellido(apellido_limpio.lower(), linea_original)
                        
                except IndexError:
                    # Esto pasa si la línea no tiene coma (ej: "Smith")
                    print(f"Línea ignorada (formato incorrecto): '{linea_limpia}'")
                except Exception as e:
                    print(f"Error procesando línea: {e}")

        print("\n¡Clasificación completada!")
        print(f"Revisa los archivos de salida.")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo de entrada '{archivo_entrada}'.")
    except Exception as e:
        print(f"Hubo un error inesperado al leer: {e}")

if __name__ == "__main__":
    main()