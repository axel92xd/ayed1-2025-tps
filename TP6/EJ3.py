archivo_alturas = "alturas_atletas.txt"
archivo_promedios = "promedios_disciplinas.txt"

def GrabarRangoAlturas():
    """
    Graba en un archivo las alturas de los atletas
    Pre: Ninguna
    Post: Crea el archivo 'alturas_atletas.txt' con el siguiente formato:
    """
    
    try:
        with open(archivo_alturas, 'wt', encoding='utf-8') as f:
            while True:
                disciplina = input("\nIngrese la disciplina (o 'fin' para terminar): ").strip()
                if not disciplina:
                    continue 
                if disciplina.lower() == 'fin':
                    break
                f.write(f"{disciplina}\n")
                
                print(f"Ingrese las alturas para {disciplina} (escriba 'fin' para parar):")
                while True:
                    altura_str = input("  Altura: ").strip()
                    if altura_str.lower() == 'fin':
                        break
                    
                    try:
                        altura_float = float(altura_str) 
                        if altura_float <= 0:
                            raise ValueError("La altura debe ser positiva.")
                        
                        f.write(f"{altura_str}\n")
                    except ValueError:
                        print("Error: Ingrese un número válido (ej: 1.85).")
                
                f.write(f"{disciplina}\n")
                
        print(f"\nArchivo '{archivo_alturas}' guardado.")
        
    except Exception as e:
        print(f"Error al grabar alturas: {e}")

def GrabarPromedio():
    """
    Lee el archivo de alturas, calcula promedios por disciplina
    y graba los resultados en otro archivo.
    Pre: El archivo 'alturas_atletas.txt' debe existir y estar bien formado.
    Post: Crea el archivo 'promedios_disciplinas.txt' con el siguiente formato:
    """
    
    try:
        with open(archivo_alturas, 'rt', encoding='utf-8-sig') as f_entrada, \
             open(archivo_promedios, 'wt', encoding='utf-8') as f_salida:
            
            linea = f_entrada.readline() # Lee la primera línea (debería ser una disciplina)
            
            while linea:
                disciplina = linea.strip()
                if not disciplina:
                    linea = f_entrada.readline()
                    continue

                suma_alturas = 0.0
                cantidad_alturas = 0
                
                while True:
                    linea_interna = f_entrada.readline()
                    
                    if not linea_interna: 
                        print(f"Error: Archivo malformado. '{disciplina}' no tiene marcador de fin.")
                        break 
                    
                    linea_interna_limpia = linea_interna.strip()
                    
                    if linea_interna_limpia == disciplina:
                        break # Encontramos el fin, salimos del bucle interno
                    
                    try:
                        suma_alturas += float(linea_interna_limpia)
                        cantidad_alturas += 1
                    except ValueError:
                        pass 

                # Calculamos y guardamos el promedio de este bloque
                if cantidad_alturas > 0:
                    promedio = suma_alturas / cantidad_alturas
                    f_salida.write(f"{disciplina}\n")
                    f_salida.write(f"{promedio:.2f}\n") 
                
                if not linea_interna:
                    break 
                    
                linea = f_entrada.readline() 
        
        print(f"Archivo '{archivo_promedios}' guardado.")
        
    except FileNotFoundError:
        print(f"Error: No se encontró '{archivo_alturas}'. Ejecutá el Paso 1 primero.")
    except Exception as e:
        print(f"Error al grabar promedios: {e}")

def MostrarMasAltos():
    """
    Lee el archivo de promedios, calcula el promedio general
    y muestra las disciplinas que lo superan. 
    """
    
    promedios_por_disciplina = {} 
    suma_total_promedios = 0.0
    
    try:
        with open(archivo_promedios, 'rt', encoding='utf-8-sig') as f:
            while True:
                disciplina = f.readline().strip()
                promedio_str = f.readline().strip()
                
                if not disciplina or not promedio_str:
                    break # Se terminó el archivo
                
                try:
                    promedio_val = float(promedio_str)
                    promedios_por_disciplina[disciplina] = promedio_val
                    suma_total_promedios += promedio_val
                except ValueError:
                    pass 
        
        if not promedios_por_disciplina:
            print("No hay datos de promedios para analizar. Ejecutá el Paso 2 primero.")
            return

        promedio_general = suma_total_promedios / len(promedios_por_disciplina)
        
        print(f"\nPromedio general de alturas: {promedio_general:.2f} mts.")
        print("Disciplinas que superan el promedio:")

        # Recorremos el diccionario y mostramos las que superan el promedio
        encontrados = 0
        for disciplina, promedio in promedios_por_disciplina.items():
            if promedio > promedio_general:
                print(f"  - {disciplina} (con {promedio:.2f} mts)")
                encontrados += 1
        
        if encontrados == 0:
            print("  (Ninguna disciplina supera el promedio general)")

    except FileNotFoundError:
        print(f"Error: No se encontró '{archivo_promedios}'. Ejecutá el Paso 2 primero.")
    except Exception as e:
        print(f"Error al mostrar promedios altos: {e}")


def main():
    GrabarRangoAlturas()
    GrabarPromedio()
    MostrarMasAltos()

if __name__ == "__main__":
    main()