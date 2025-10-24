import random
import os


class Barco:
    """
    Representa un barco en el juego.
    Contiene una lista ordenada de casillas que forman el barco y sus puntos de vida.
    """
    def __init__(self, longitud):
        # longitud del barco en casillas
        self.longitud = longitud
        # Puntos de vida iniciales iguales al longitud del barco. Se usa para saber cuándo decir que un barco fue hundido.
        self.puntos_vida = longitud

    def recibe_impacto(self):
        """
        Maneja cuando una parte de este barco es disparada.
        Reduce los puntos de vida y devuelve True si el barco está ahora hundido.
        """
        self.puntos_vida -= 1
        return self.puntos_vida <= 0  # devuelve True si el barco está hundido



class Casilla:
    """
    Representa una sola casilla en el tablero de juego.
    Contiene información sobre qué se muestra cuando la casilla es visible y después de ser disparada.
    """
    def __init__(self, char_por_defecto, char_disparo):
        """
        Tiene un carácter por defecto dependiando de su contenido y otro si se dispara.
        Si la variable barco está establecida, entonces esta casilla pertenece a un barco, de lo contrario es agua
        """
        self.char = char_por_defecto
        self.char_disparo = char_disparo
        self.barco = None
        self.ha_sido_disparada = False

    def es_disparada(self):
        """
        Gestiona cuando esta casilla es disparada.
        Devuelve True si fue un nuevo disparo (no disparado previamente), False en caso contrario.
        """

        if self.ha_sido_disparada:
            return False
        else:
            self.ha_sido_disparada = True
            # Cuando es disparada, cambiar el carácter mostrado al carácter de disparo
            self.char = self.char_disparo
            return True




class Tablero: 
    """
    Crea un tablero de 10x10 y lo popula con el objeto casilla.
    """
    def __init__(self):
        # Crear una cuadrícula 10x10 de casillas de agua inicialmente
        self.grid = []
        for fila in range(10):
            fila_grid = [] 
            for columna in range(10):
                # Casilla de agua con '~' como carácter visible y '@' cuando es disparada
                fila_grid.append(Casilla('~', 'w'))
            self.grid.append(fila_grid)


    def es_colocacion_valida(self, fila_inicio, columna_inicio, direccion, longitud):
        """
        Verifica si un barco puede colocarse en la posición especificada sin superponerse
        a otros barcos o salirse de los límites. Los barcos necesitan al menos 1 casilla de espacio de otros barcos.
        """
        # Calcular el área de colocación para todo el barco con 1 casilla de buffer alrededor
        if direccion == 'H':
            fila_min = max(0, fila_inicio - 1)
            fila_max = min(10, fila_inicio + 2)  # +2 porque el rango es exclusivo en el límite superior
            columna_min = max(0, columna_inicio - 1)
            columna_max = min(10, columna_inicio + longitud + 1)  # +longitud para longitud del barco, +1 para buffer
        else:  # direccion == 'V'
            fila_min = max(0, fila_inicio - 1)
            fila_max = min(10, fila_inicio + longitud + 1)  # +longitud para longitud del barco, +1 para buffer
            columna_min = max(0, columna_inicio - 1)
            columna_max = min(10, columna_inicio + 2)  # +2 porque el rango es exclusivo en el límite superior

        # Verificar si alguna casilla en el área de colocación tiene un barco
        for r in range(fila_min, fila_max):
            for c in range(columna_min, columna_max):
                if self.grid[r][c].barco:
                    return False

        return True



class Jugador:
    """
    Crea los jugadores y prepara sus tableros 

    Representa un jugador en el juego.
    Contiene la flota del jugador, puntos de vida, y métodos para verificar si el jugador perdió.
    """
    def __init__(self):
        self.puntos_vida = 0 # cada barco añadido hará +1

    def preparar_flota(self):
        """
        Crea el tablero con la flota del jugador:
        - 1 barco de 4
        - 2 barcos de 3  
        - 3 barcos de 2
        """
        self.mapa = Tablero()

        longitudes_barcos = [4, 3, 3, 2, 2, 2]  # [grande, mediano, mediano, pequeño, pequeño, pequeño]

        for longitud in longitudes_barcos:
            barco = Barco(longitud)
            colocado = False
            
            # Seguir intentando colocar el barco hasta que se encuentre una colocación válida
            while not colocado:
                direccion = random.choice(['H', 'V'])  # H=horizontal, V=vertical
                # Elegir aleatoriamente posición inicial y dirección
                if direccion == 'H':
                    fila_inicio = random.randint(0, 9)
                    columna_inicio = random.randint(0, 10 - barco.longitud)
                else:  # direccion == 'V'
                    fila_inicio = random.randint(0, 10 - barco.longitud)
                    columna_inicio = random.randint(0, 9)

                
                # Verificar si la colocación es válida
                if self.mapa.es_colocacion_valida(fila_inicio, columna_inicio, direccion, longitud):
                    # Colocar las casillas del barco en la cuadrícula
                    for i in range(barco.longitud):
                        if direccion == 'H':
                            fila, columna = fila_inicio, columna_inicio + i
                        else:  # direccion == 'V'
                            fila, columna = fila_inicio + i, columna_inicio

                        casilla_barco = Casilla('O', '✷')
                        casilla_barco.barco = barco  # Enlazar la casilla al barco
                        self.mapa.grid[fila][columna] = casilla_barco
                    
                    self.puntos_vida += 1
                    colocado = True

    def ha_perdido(self):
        """
        Verifica si el jugador ha perdido (puntos de vida llegaron a 0).
        """
        return self.puntos_vida <= 0

    def recibe_disparo(self, fila, columna):
        """
        Maneja cuando este jugador es disparado en la coordenada especificada.
        Devuelve tupla: (disparo_exitoso, barco_hundido).
        """
        # Obtener la casilla en esta posición
        casilla = self.mapa.grid[fila][columna]
        
        # disparar la casilla y ver si es un nuevo disparo
        es_nuevo_disparo = casilla.es_disparada()
        
        # Si esto no es un nuevo disparo (ya disparado), retornar inmediatamente
        if not es_nuevo_disparo:
            return (False, False)
        
        # si hay un barco
        if casilla.barco:
            # el barco pierde 1 punto de vida y devuelve si se ha hundido
            barco_hundido = casilla.barco.recibe_impacto()
            if barco_hundido:
                self.puntos_vida -= 1
            return (True, barco_hundido)
        else:
            # es un fallo (casilla de agua)
            return (False, False)



def renderizar_mapas(usuario, python):
    """
    Muestra los dos mapas con coordenadas.
    El del jugador tiene visibilidad completa; el del ordenador aparece oculto.
    """
    # borra la terminal para que no sea scroll infinito
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # banner
    print("=" * 50)
    print("             🚢   HUNDIR LA FLOTA  🚢")
    print("=" * 50)
    # estado
    print(f"    Barcos a flote : {usuario.puntos_vida}       Barcos a flote: {python.puntos_vida}")
    print()
    
    # letras de columna
    print("   A B C D E F G H I J      A B C D E F G H I J")
    
    # números de fila
    for r in range(10):
        # número de fila para mapa usuario
        print(f"{r+1:2}", end=" ")
        # casillas del mapa usuario
        for c in range(10):
            print(usuario.mapa.grid[r][c].char, end=" ")

        print("  ", end="")  # Espacio entre mapas

        # número de fila para mapa ord
        print(f"{r+1:2}", end=" ")
        # casillas del mapa ord
        for c in range(10):
            #print(python.mapa.grid[r][c].char, end=" ")

            if python.mapa.grid[r][c].ha_sido_disparada == True:
                print(python.mapa.grid[r][c].char, end=" ")
            else:
                print("·", end=" ")

        print()


def mostrar_mapa_completo(usuario, python):
    """
    Muestra los dos mapas con coordenadas.
    Visibilidad completa.
    """
    # borra la terminal para que no sea scroll infinito
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # banner
    print("=" * 50)
    print("             🚢      RESULTADO    🚢")
    print("=" * 50)
    # estado
    print(f"    Barcos a flote : {usuario.puntos_vida}       Barcos a flote: {python.puntos_vida}")
    print()
    
    # letras de columna
    print("   A B C D E F G H I J      A B C D E F G H I J")
    
    # números de fila
    for r in range(10):
        # número de fila para mapa usuario 
        print(f"{r+1:2}", end=" ")
        # casillas del mapa usuario
        for c in range(10):
            print(usuario.mapa.grid[r][c].char, end=" ")

        print("  ", end="")  # espacio entre mapas

        # número de fila para mapa ord 
        print(f"{r+1:2}", end=" ")
        # casillas del mapa ord
        for c in range(10):
            print(python.mapa.grid[r][c].char, end=" ")

        print()


def analizar_coordenada(str_coordenada):
    """
    Analiza un string de coordenada como 'A1' para convertir en índices de fila y columna.
    Devuelve (fila, columna) o (None, None) si es inválida.
    """
    str_coordenada = str_coordenada.strip().upper()
    
    # no puede tener más de tres ch (a1 - a10)
    if len(str_coordenada) < 2 or len(str_coordenada) > 3:
        return (None, None)
    
    # separar partes de letra y número
    parte_letra = ""
    parte_numero = ""
    
    for char in str_coordenada:
        if char.isalpha():
            parte_letra += char
        elif char.isdigit():
            parte_numero += char
    
    # validar partes
    if len(parte_letra) != 1 or len(parte_numero) == 0:
        return (None, None)
    
    # convertir a índices
    columna = ord(parte_letra[0]) - ord('A')
    fila = int(parte_numero) - 1
    
    # validar rango
    if fila < 0 or fila > 9 or columna < 0 or columna > 9:
        return (None, None)
    
    return (fila, columna)
