 # Juego_Ahorcado
        #  Juego del Ahorcado con Categorías – Python

    Este proyecto implementa un **juego del ahorcado por consola**, con:
    - Selección de **categorías**,
    - Dibujo ASCII del ahorcado,
    - Soporte para **múltiples jugadores** mediante apodos,
    - **Registro persistente** de puntajes,
    - Sistema de **Top 10** basado en victorias.

    ## Estructura del Proyecto

    proyecto_ahorcado/
    ├── ahorcado.py        # Código principal del juego
    ├── palabras.txt       # Lista de palabras organizadas por categorías
    ├── puntajes.txt       # Registro de jugadores: apodo,victorias,derrotas
    └── README.md          # Documentación del proyecto

    ##  Características principales

    ### Gestión de jugadores
    - Cada jugador ingresa un **apodo único**.
    - Se registran automáticamente:
    - Victorias  
    - Derrotas
    - Los datos se guardan en `puntajes.txt`.

    ### Mecánica del juego
    - Se muestran categorías disponibles.
    - El jugador elige una categoría.
    - Se selecciona una palabra aleatoria.
    - El jugador tiene **6 intentos**.

    Durante la partida se muestran:
    - Dibujo ASCII del ahorcado,
    - Letras acertadas,
    - Letras incorrectas,
    - Intentos restantes.

    ###  Sistema de puntuación
    - Archivo `puntajes.txt` actualizado automáticamente.
    - Opción de menú para ver el **Top 10** clasificado por número de victorias.

    ## Archivos usados

    ### **palabras.txt**
    Formato:

    categoria:palabra
    categoria:palabra

    ### **puntajes.txt**
    Se genera automáticamente si no existe.  
    Formato:
    
    apodo,victorias,derrotas

    ## Cómo ejecutar el juego

    1. Clona o descarga el repositorio

    2. Asegúrate de que estén los archivos:
    -palabras.txt
    -puntajes.txt   (se genera automáticamente si no existe)

    3. Ejecuta el juego:
    
    python ahorcado.py

    ## Menú principal

    Al iniciar se muestra:

    --- AHORCADO ---
    1. Jugar
    2. Ver Top 10
    3. Salir

    ### 1-Jugar
    - Se ingresa un apodo único.
    - Se elige una categoría.
    - Se juega la partida.
    - Se registran victorias y derrotas.

    ### 2-Ver Top 10
    - Muestra un ranking basado **solo en victorias acumuladas**.

    ### 3- Salir
    - Finaliza la ejecución del juego.
