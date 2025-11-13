

def convertir_formato_1(archivo_entrada, f_salida_csv):
    """
    Lee el archivo de formato 1 (longitud fija).
    Escribe en el archivo CSV (manual).
    
    Pre:  archivo_entrada (str), f_salida_csv (manejador de archivo abierto)
    Post: Escribe los datos en f_salida_csv
    """
    print(f"Procesando Formato 1 ({archivo_entrada})...")
    try:
        with open(archivo_entrada, 'rt', encoding='utf-8') as f_in:
            for linea in f_in:
                linea_limpia = linea.rstrip('\n') # Quitamos solo el salto de línea
                if not linea_limpia.strip(): # Ignoramos líneas vacías
                    continue
                
                # Cortamos la línea 
                apellido_nombre = linea_limpia[0:20].strip()
                fecha_alta = linea_limpia[21:29].strip()
                domicilio = linea_limpia[30:].strip() # Desde la 30 hasta el final
                
                # Creamos la lista y la escribimos manualmente
                fila_lista = [apellido_nombre, fecha_alta, domicilio]
                f_salida_csv.write(",".join(fila_lista) + "\n")
        
        print("Formato 1 procesado con éxito.")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Error procesando Formato 1: {e}")

def convertir_formato_2(archivo_entrada, f_salida_csv):
    """
    Lee el archivo de formato 2 (campos con longitud).
    Escribe en el archivo CSV (manual).
    
    Pre:  archivo_entrada (str), f_salida_csv (manejador de archivo abierto)
    Post: Escribe los datos en f_salida_csv
    """
    print(f"Procesando Formato 2 ({archivo_entrada})...")
    try:
        with open(archivo_entrada, 'rt', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                
                campos_de_la_fila = []
                puntero = 0 # El puntero es dónde estamos parados en la línea
                
                while puntero < len(linea):
                    
                    # 1. Leemos los 2 dígitos de la longitud
                    try:
                        longitud_str = linea[puntero : puntero + 2]
                        longitud_campo = int(longitud_str)
                        puntero += 2 # Movemos el puntero 2 lugares
                    except Exception:
                        print(f"Error de formato en línea (se esperaba longitud): {linea}")
                        break # Saltamos esta línea

                    # 2. Leemos el dato (según la longitud que acabamos de leer)
                    if puntero + longitud_campo > len(linea):
                        print(f"Error de formato en línea (longitud incorrecta): {linea}")
                        break
                        
                    dato = linea[puntero : puntero + longitud_campo]
                    puntero += longitud_campo # Movemos el puntero
                    
                    campos_de_la_fila.append(dato)
                
                # Escribimos la fila manualmente (si encontramos campos)
                if campos_de_la_fila:
                    f_salida_csv.write(",".join(campos_de_la_fila) + "\n")
        
        print("Formato 2 procesado con éxito.")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Error procesando Formato 2: {e}")

def main():
    
    formato_1= "formato_1.txt"
    formato_2 = "formato_2.txt"
    archivo_csv = "empleados_manual.csv" # 
    
    print("--- Ejercicio 5: Conversor de Formatos a CSV (Manual) ---")
    
    while True:
        print("\n¿Qué formato desea convertir?")
        print("1. Formato 1 (Longitud Fija)")
        print("2. Formato 2 (Longitud Variable)")
        print("0. Salir")
        opcion = input("Seleccione: ").strip()
        
        if opcion == '1' or opcion == '2':
            # Preparamos el archivo CSV de salida (en modo 'wt' para sobrescribir)
            try:
                # 'wt' = Write Text. Abrimos el archivo de salida UNA SOLA VEZ
                with open(archivo_csv, 'wt', encoding='utf-8') as f_salida_csv:
                    
                    # Escribimos el encabezado manualmente
                    f_salida_csv.write("Apellido y Nombre,Fecha de Alta,Domicilio\n")
                    
                    if opcion == '1':
                        convertir_formato_1(formato_1, f_salida_csv)
                    else:
                        convertir_formato_2(formato_2, f_salida_csv)
                        
                print(f"\n¡Archivo '{archivo_csv}' generado con éxito!")
                
            except Exception as e:
                print(f"Error al escribir el archivo CSV: {e}")
        
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    # Creamos archivos de ejemplo para probar
    try:
        with open("formato_1.txt", "w", encoding="utf-8") as f:
            f.write("Pérez Juan       20080211 Corrientes 348                   \n")
            f.write("González Ana M   20080115 Juan de Garay 1111 3er piso dto A\n")
        
        with open("formato_2.txt", "w", encoding="utf-8") as f:
            f.write("10Pérez Juan082008021114Corrientes 348\n")
            f.write("14González Ana M082008011533Juan de Garay 1111 3er piso dto A\n")
        print("Archivos de ejemplo (formato_1.txt, formato_2.txt) creados.")
    except Exception as e:
        print(f"Error al crear archivos de ejemplo: {e}")

    main()