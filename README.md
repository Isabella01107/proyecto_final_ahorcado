 # Juego_Ahorcado
    # 🕹️ Juego del Ahorcado en Python

    Este proyecto implementa un juego del ahorcado por consola, con soporte para múltiples jugadores mediante apodos, registro persistente de puntajes y un sistema de Top 10.

    El juego selecciona palabras al azar desde un archivo de texto y almacena victorias y derrotas en un archivo separado.

    ## Estructura del Proyecto
    proyecto_ahorcado/ 
    ├── ahorcado.py # Código principal del juego 
    ├── palabras.txt # Lista de palabras para jugar 
    ├── puntajes.txt # Registro de jugadores y sus resultados 
    └── README.md # Documentación del proyecto

    #Características principales

    ##Gestión de jugadores
    - Cada jugador ingresa un apodo único.
    -Se registran automáticamente victorias y derrotas en un archivo persistente.
    
    ##Mecánica del juego
    -Selección aleatoria de palabras desde palabras.txt.
    -El jugador tiene 6 intentos para adivinar la palabra.
    Se muestran:
    -Letras acertadas
    -Letras incorrectas
    -Intentos restantes

    ##Sistema de puntuación
    -Archivo puntajes.txt actualizado automáticamente.
    -Disponible un menú para ver el Top 10 de jugadores con más victorias.
    
    #Archivos usados
    
    -palabras.txt → contiene las palabras del ahorcado.
    -puntajes.txt → guarda: apodo,victorias,derrotas
    
    #Cómo ejecutar el juego
    
    1.Clona o descarga el repositorio
    2.Asegúrate de que existan los archivos:
    -palabras.txt
    -puntajes.txt   (se genera automáticamente si no existe)
    3.Ejecuta el juego:
    python ahorcado.py
    
    #Formato de los archivos

    ##palabras.txt
    -Lista de palabras, una por línea (sin comas)

    ##puntajes.txt
    -Generado automáticamente con este formato:

    Menú principal
    Al ejecutar el juego aparecerá:
    --- AHORCADO ---
    1. Jugar
    2. Ver Top 10
    3. Salir
    
    1-Jugar
    -Se pide un apodo
    -Se inicia la partida
    -Se registran victorias/derrotas
    
    2-Ver Top 10
    -Se muestra un ranking basado en la cantidad de victorias
    
    3-Salir
    -Finaliza la ejecución


