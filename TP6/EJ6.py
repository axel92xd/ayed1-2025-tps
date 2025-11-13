import datetime 
import random   

# --- Constantes ---
archivo_huespedes = 'huespedes_manual.csv'
pisos_totales = 10
habitaciones_por_piso = 6

#Funciones de Validación 

def validar_fecha(fecha_str: str) -> bool:
    """Verifica si una fecha DDMMAAAA es válida (formato simple)."""
    if len(fecha_str) != 8 or not fecha_str.isdigit():
        return False
    try:
        # Intentamos crear una fecha (esto falla con ej: 30022024)
        datetime.datetime.strptime(fecha_str, "%d%m%Y")
        return True
    except ValueError:
        return False

def convertir_a_fecha(fecha_str: str) -> datetime.date:
    """Convierte un string DDMMAAAA a un objeto fecha (date)."""
    return datetime.datetime.strptime(fecha_str, "%d%m%Y").date()


def registrar_ingresos():
    """
    Registra el ingreso de huéspedes en un CSV (manual).
    Valida DNI (no repetido en la sesión) y fechas.
    Termina cuando el DNI es -1.
    """
    print("--- Parte 1: Registro de Huéspedes (CSV Manual) ---")
    
    dnis_registrados = set()
    
    try:
        with open(archivo_huespedes, 'wt', encoding='utf-8') as f_csv:
            
            # Escribimos el encabezado manualmente
            f_csv.write("DNI,Apellido y Nombre,Fecha Ingreso,Fecha Egreso,Ocupantes\n")
            
            print("Ingrese los datos del huésped (DNI -1 para terminar):")
            
            while True:
                # Pedir DNI 
                try:
                    dni_str = input("\nIngrese DNI del cliente (-1 para salir): ").strip()
                    dni = int(dni_str)
                except ValueError:
                    print("Error: El DNI debe ser un número entero.")
                    continue
                
                if dni == -1:
                    break
                
                if dni in dnis_registrados:
                    print("Error: El DNI ya fue ingresado en esta sesión.")
                    continue
                
                # Pedir Resto de Datos
                nombre = input("Ingrese Apellido y Nombre: ").strip()
                # Validacion para csv
                if not nombre or "," in nombre:
                    print("Error: El nombre no puede estar vacío ni contener comas.")
                    continue

                fecha_ingreso_str = input("Fecha de Ingreso (DDMMAAAA): ").strip()
                fecha_egreso_str = input("Fecha de Egreso (DDMMAAAA): ").strip()

                try:
                    ocupantes_str = input("Cantidad de Ocupantes: ").strip()
                    ocupantes = int(ocupantes_str)
                    if ocupantes <= 0:
                         print("Error: Los ocupantes deben ser al menos 1.")
                         continue
                except ValueError:
                    print("Error: La cantidad de ocupantes debe ser un número.")
                    continue

                # Validamos Fechas 
                if not validar_fecha(fecha_ingreso_str) or not validar_fecha(fecha_egreso_str):
                    print("Error: Formato de fecha incorrecto o fecha inválida.")
                    continue
                
                # Convertimos a objetos fecha para comparar
                fecha_ingreso = convertir_a_fecha(fecha_ingreso_str)
                fecha_egreso = convertir_a_fecha(fecha_egreso_str)
                    
                if fecha_egreso <= fecha_ingreso:
                    print("Error: La fecha de egreso debe ser mayor que la de ingreso.")
                    continue
                
                # Guardamos los datos 
                fila_lista = [dni_str, nombre, fecha_ingreso_str, fecha_egreso_str, ocupantes_str]
                f_csv.write(",".join(fila_lista) + "\n")
                
                dnis_registrados.add(dni)
                print(f"Huésped '{nombre}' registrado con éxito.")

        print(f"\nDatos guardados en '{archivo_huespedes}'.")

    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")


def procesar_reportes():
    """
    Lee 'huespedes.csv' (manualmente) y realiza todos los
    cálculos y reportes (a, b, c, d, e, f).
    """
    print("\n--- Parte 2: Reportes y Asignación de Habitaciones ---")
    
    # --- a. Crear la estructura del hotel ---
    # Una lista de listas (matriz) 10x6
    hotel = [[0] * habitaciones_por_piso for _ in range(pisos_totales)]
    habitaciones_libres = pisos_totales * habitaciones_por_piso
    
    huespedes_para_reportes = [] # Para guardar los datos leídos
    
    try:
        with open(archivo_huespedes, 'rt', encoding='utf-8-sig') as f_csv:
            
            f_csv.readline() # Saltamos el encabezado manualmente
            
            for linea in f_csv:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                
                try:
                    partes = linea_limpia.split(',')
                    if len(partes) != 5: continue # Ignoramos líneas malformadas
                    
                    # Convertimos los datos
                    dni = int(partes[0])
                    nombre = partes[1]
                    fecha_ingreso = convertir_a_fecha(partes[2])
                    fecha_egreso = convertir_a_fecha(partes[3])
                    ocupantes = int(partes[4])
                    
                    # (f) Calculamos días
                    dias_alojamiento = (fecha_egreso - fecha_ingreso).days
                    
                    # Guardamos los datos leídos
                    huespedes_para_reportes.append({
                        'nombre': nombre,
                        'fecha_egreso': fecha_egreso,
                        'ocupantes': ocupantes,
                        'dias': dias_alojamiento
                    })
                    
                    # Asignar habitación (arbitrariamente) 
                    if habitaciones_libres > 0:
                        asignada = False
                        while not asignada:
                            piso_azar = random.randint(0, pisos_totales - 1)
                            hab_azar = random.randint(0, habitaciones_por_piso - 1)
                            if hotel[piso_azar][hab_azar] == 0:
                                hotel[piso_azar][hab_azar] = ocupantes
                                habitaciones_libres -= 1
                                asignada = True
                    
                except (ValueError, IndexError):
                    print(f"Ignorando línea (error al procesar): {linea_limpia}")
        
        # Fin de la lectura. Ahora generamos los reportes 
        
        if not huespedes_para_reportes:
            print("No hay huéspedes registrados para generar reportes.")
            return

        # b. Piso con mayor cantidad de habitaciones ocupadas 
        # d. Piso con mayor cantidad de personas 
        # (Hacemos b y d en el mismo bucle) 
        piso_mas_ocupado = -1
        max_ocupadas = -1
        piso_mas_personas = -1
        max_personas = -1
        
        for i, piso in enumerate(hotel): # i es el nro de piso (0-9)
            ocupadas_en_piso = 0
            personas_en_piso = 0
            for ocupantes_hab in piso:
                personas_en_piso += ocupantes_hab
                if ocupantes_hab > 0:
                    ocupadas_en_piso += 1
            
            if ocupadas_en_piso > max_ocupadas:
                max_ocupadas = ocupadas_en_piso
                piso_mas_ocupado = i + 1 # (Sumamos 1 pq los pisos son 1-10)
                
            if personas_en_piso > max_personas:
                max_personas = personas_en_piso
                piso_mas_personas = i + 1

        print(f"b. Piso con más habs ocupadas: Piso {piso_mas_ocupado} ({max_ocupadas} habs)")
        print(f"d. Piso con más personas: Piso {piso_mas_personas} ({max_personas} personas)")

        # Cuántas habitaciones vacías hay
        print(f"c. Habitaciones vacías en el hotel: {habitaciones_libres}")

        # Próxima habitación en desocuparse 
        try:
            fecha_actual_str = input("\nIngrese fecha actual (DDMMAAAA) para reporte 'e': ").strip()
            fecha_actual = convertir_a_fecha(fecha_actual_str)
            
            proxima_fecha_egreso = None
            huespedes_proximos = []
            
            for h in huespedes_para_reportes:
                if h['fecha_egreso'] > fecha_actual:
                    if proxima_fecha_egreso is None or h['fecha_egreso'] < proxima_fecha_egreso:
                        proxima_fecha_egreso = h['fecha_egreso']
                        huespedes_proximos = [h['nombre']]
                    elif h['fecha_egreso'] == proxima_fecha_egreso:
                        huespedes_proximos.append(h['nombre'])

            if not proxima_fecha_egreso:
                print("e. No hay egresos programados después de hoy.")
            else:
                print(f"e. Próximos en desocuparse (el {proxima_fecha_egreso.strftime('%d/%m/%Y')}):")
                for nombre in huespedes_proximos:
                    print(f"   - {nombre}")
        except ValueError:
            print("Fecha inválida. Omitiendo reporte 'e'.")


        # Listado ordenado por días de alojamiento 
        print("\nf. Listado de huéspedes ordenado por días de alojamiento:")
        
        huespedes_ordenados = sorted(huespedes_para_reportes, key=lambda h: h['dias'])
        
        for h in huespedes_ordenados:
            print(f"   - {h['nombre']} ({h['dias']} días)")

    except FileNotFoundError:
        print(f"Error: No se encontró '{archivo_huespedes}'. Ejecute el Paso 1 primero.")
    except Exception as e:
        print(f"Error inesperado al procesar reportes: {e}")


def main():
    """
    Programa principal que ejecuta los 2 pasos en orden.
    Pre:  Ninguna.
    Post: Ejecuta el registro de ingresos y luego procesa los reportes.
    """
    registrar_ingresos()
    print("\n" + "=" * 40)
    
    input("Datos guardados. Presione Enter para procesar reportes...")
    procesar_reportes() 

if __name__ == "__main__":
    main() 

