import time

def contador_interrumpible():
    """
    Imprime números del 1 al 100000.
    Solicita confirmación antes de salir si se presiona Ctrl-C.
    
    Pre:  Inicia un bucle de impresión.
    Post: Imprime números. Si se captura KeyboardInterrupt,
          el bucle se detiene (running=False) solo si el usuario
          confirma con 's'.
    """
    print("Iniciando conteo (Presione Ctrl-C para intentar interrumpir)...")
    
    i = 1
    running = True # Usamos una bandera para controlar el bucle
    
    while i <= 100000 and running:
        try:
            # Imprime y vuelve al inicio de la línea (\r) para no saturar la consola
            print(i, end=" \r") 
            time.sleep(0.001) # Pequeña pausa para ver el conteo
            i += 1
        except KeyboardInterrupt:
            print("\n¡Interrupción detectada (Ctrl-C)!")
            confirm = input("¿Seguro que desea detener el programa? (s/n): ")
            if confirm.lower() == 's':
                running = False # La bandera se pone en False y el bucle termina
                print("Proceso detenido por el usuario.")
            else:
                print("Reanudando...")
                
    if running: # Si terminó el bucle sin interrupción
        print("\nConteo finalizado.")

def main():
    """
    Programa principal para probar la función contador_interrumpible.
    Pre: No recibe parámetros.  
    Post: Ejecuta el contador interrumpible.
    """

    contador_interrumpible()

if __name__ == "__main__":
    main()