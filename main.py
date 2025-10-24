from utils import *
import random
import time

# bienvenida
print("¡Hola, soy Python! ¡Vamos a jugar a hundir la flota!")
time.sleep(1)
print(f"En seguida estará listo el juego :)")
time.sleep(2)

# crear jugadores
python = Jugador()
usuario = Jugador()

# flota ordenador
python.preparar_flota()

# preparar flota usuario
while True:
    usuario.preparar_flota()
    
    # mostrar la disposición inicial del mapa
    renderizar_mapas(usuario, python)
    
    # preguntar si el jugador quiere recolocar o empezar el juego
    print()
    eleccion_usuario = input("Presiona 'R' para recolocar barcos, o 'ENTER' para empezar el juego: ").strip().upper()
    
    if eleccion_usuario != 'R':
        break  # salir del bucle, barcos fijados

# determinar quién va primero aleatoriamente
print("¡Lanzamiento de moneda!")
jugador_actual = random.choice([usuario, python])
time.sleep(1)
print("...")
time.sleep(1)
if jugador_actual == usuario:
    print(f"¡Empiezas tú!")
else:
    print(f"¡Empiezo yo!")

time.sleep(1)

# bucle juego
while True: # mientra el juego esté en curso

    renderizar_mapas(usuario, python) #constante
    
    if jugador_actual == usuario: # turno del usuario
        print()
        print("Ingresa coordenada (ej: A1) o 'Q' para salir: ", end="")
        entrada_usuario = input().strip().upper()
        
        if entrada_usuario == 'Q':
            break
        
        # analizar input                
        fila, columna = analizar_coordenada(entrada_usuario)
        
        if fila is None or columna is None:
            print("Coordenadas inválidas. Usa formato como A5, B3, etc.")
            time.sleep(2)
            continue
        
        # verificar si esta casilla ya fue disparada
        if python.mapa.grid[fila][columna].ha_sido_disparada:
            print("¡Ya has disparado aquí! Elige otra coordenada.")
            time.sleep(2)
            continue
        
        # disparar!!!
        disparo_exitoso, barco_hundido = python.recibe_disparo(fila, columna)
        time.sleep(1)

        # mostrar resultado
        if disparo_exitoso:
            if barco_hundido:
                print("¡Hundido!")
                time.sleep(1)
                
                if python.ha_perdido():
                    renderizar_mapas(usuario, python)
                    print(f"\n¡Felicidades! Has hundido todos mis barcos. ¡Ganas tú!")
                    time.sleep(2)
                    break
            else:
                print("¡Tocado!")
            jugador_actual = usuario
        else:
            print("¡Agua!")
            time.sleep(1)
            # cambiar al turno del ordenador
            jugador_actual = python
            print("¡Me toca!")
        
        # esperar antes del turno del ordenador
        time.sleep(1)
        
    else:  # turno de python
        print("\nHmm...")

        while True:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
        
            # prueba casillas al azar
            casilla = usuario.mapa.grid[fila][columna]
            if not casilla.ha_sido_disparada:
                break  # encuentra una casilla no disparada
    
        # dispara y recoge el feedback
        disparo_exitoso, barco_hundido = usuario.recibe_disparo(fila, columna)
        
        str_coordenada = chr(ord('A') + columna) + str(fila + 1)
        
        time.sleep(1)
    
        # resultado
        if disparo_exitoso:
            if barco_hundido:
                print(f"¡{str_coordenada}!")
                time.sleep(1)
                print("¿Hundido?")
                time.sleep(1)
                print("¡Bieen!")
                time.sleep(2)
                # Verificar si el jugador usuario ha perdido
                if usuario.ha_perdido():
                    renderizar_mapas(usuario, python)
                    print("\n¡He acabado con tus barcos! He tenido suerte :D")
                    break
            else:
                print(f"¡{str_coordenada}!")
                time.sleep(1)
                print("¿Tocado?")
                time.sleep(1)
                print("¡Sigo!")
                time.sleep(2)
            jugador_actual = python

        else:
            print(f"¡{str_coordenada}!") 
            time.sleep(1)
            print("¿Agua?")
            time.sleep(1)
            print("¡Vale!")

            jugador_actual = usuario # cambiar al turno del usuario
            print("¡Te toca!")

        time.sleep(2)

mostrar_mapa_completo(usuario,python)
print("¡Gracias por jugar!")
