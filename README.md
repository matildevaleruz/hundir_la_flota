# Hundir la Flota - Juego en Python

## Descripción

Este proyecto es una implementación del clásico juego "Hundir la Flota" (Battleship) desarrollado en Python como parte del bootcamp de The Bridge de Data Science. Permite a un jugador competir contra el ordenador en una batalla naval mediante CLI.


## Características Principales

- Juego por turnos contra la computadora
- Generación automática de flotas
- 6 barcos por jugador (tamaños 4, 3, 3, 2, 2, 2)
- Interfaz clara con dos mapas visibles
- Sistema de coordenadas intuitivo (A1, B5, etc.)

## Arquitectura del Proyecto

El proyecto está estructurado siguiendo una arquitectura orientada a objetos con esta jerarquía:

### Jerarquía de Clases

Jugador → Tablero → Casilla → Barco

### Descripción de Clases

- **`Barco`**: Representa cada embarcación con su longitud y puntos de vida
- **`Casilla`**: Gestiona el estado individual de cada posición del tablero
- **`Tablero`**: Controla la cuadrícula 10x10 y la validación de colocaciones
- **`Jugador`**: Maneja la flota completa, puntos de vida y lógica del juego

## Características Técnicas 

### Validación de Colocación
El sistema asegura que los barcos:
- No se superpongan
- Mantengan al menos 1 casilla de separación
- Permanezcan dentro de los límites del tablero

### Sistema de Coordenadas
- Conversión inteligente de formato letra-número (A1) a índices de matriz
- Validación de entrada del usuario
- Prevención de disparos duplicados

### Interfaz de Usuario
- Mapas actualizados después de cada movimiento
- Indicadores visuales claros del estado del juego
- Mensajes informativos de resultado

## Archivos del Proyecto

- **`main.py`**: Contiene el flujo principal del juego y la lógica de turnos
- **`utils.py`**: Implementa todas las clases y funciones auxiliares

## Cómo Ejecutar

```bash
python main.py
```

## Cómo jugar

```bash
python main.py
```

El juego guía al jugador paso a paso:
1. Se generan automáticamente las flotas
2. Puedes recolocar barcos si lo deseas
3. Se sortea quién empieza
4. Por turnos, introduce coordenadas para disparar
    - **"Agua"**: Disparo fallido
    - **"Tocado"**: Impacto en un barco
    - **"Hundido"**: Todas las casillas de un barco han sido impactadas
5. Gana el primero que hunda toda la flota enemiga


## Reflexión sobre el Desarrollo

Este proyecto ha sido mi primera inmersión en programación orientada a objetos. Los conceptos iniciales de POO me resultaron complejos de manejar, especialmente entender cómo conectar las diferentes clases y hacer que interactuaran correctamente. Sin embargo, cada obstáculo superado se convirtió en un aprendizaje significativo.

Hubo un momento clave cuando descubrí la jerarquía natural de clases: Jugador → Tablero → Casilla → Barco. Ver cómo esta estructura se traducía directamente en código y cómo de este modo cada componente encontraba su lugar de forma lógica fue un momento eureka. Empezar por la clase más básica (Barco) y construir progresivamente hacia arriba hizo que la arquitectura emergiera de forma natural, facilitando enormemente la organización y las dependencias entre componentes.

Hay aspectos que podrían mejorarse, como implementar una IA más inteligente (que busque alrededor de los tocados en lugar de disparar aleatoriamente) o permitir la colocación manual de barcos. Sin embargo, para ser mi primer proyecto con POO, estoy muy contenta con el resultado final. Ver el juego funcionando correctamente después de tantas horas de trabajo ha hecho que cada error de indentación y cada lógica repensada valieran la pena.

---

* Mi primer proyecto OOP - hecho con Python 3 y terquedad como motor de aprendizaje *

---

PD: he incliudo unos archivos demo para poder ejecutar el loop completo más rápidamente.