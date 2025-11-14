import random
import os
AHORCADO = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]

# ------------------ Manejo de archivos ------------------

def cargar_palabras(ruta="palabras.txt"):
    """
    Carga las palabras desde un archivo de texto con formato 'categoria:palabra'.

    Retorna:
        dict: Diccionario {categoria: [palabras]}.
    """
    categorias = {}
    if not os.path.exists(ruta):
        print("No se encontró palabras.txt")
        return {}
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(":")
            if len(partes) == 2:
                categoria, palabra = partes
                categoria, palabra = categoria.lower(), palabra.lower()
                if categoria not in categorias:
                    categorias[categoria] = []
                categorias[categoria].append(palabra)
            else:
                print(f"Línea inválida en palabras.txt: {linea.strip()}")
    return categorias

def cargar_puntajes(ruta="puntajes.txt"):
    """
    Carga los puntajes desde un archivo de texto.

    Retorna:
        dict: Diccionario con formato {apodo: [victorias, derrotas]}.
    """
    puntajes = {}
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    apodo, v, d = partes
                    puntajes[apodo] = [int(v), int(d)]
    return puntajes

def guardar_puntajes(puntajes, ruta="puntajes.txt"):
    """
    Guarda los puntajes en un archivo de texto.

    Parámetros:
        puntajes (dict): Diccionario con los puntajes de los jugadores.
    """
    with open(ruta, "w", encoding="utf-8") as f:
        for apodo, (v, d) in puntajes.items():
            f.write(f"{apodo},{v},{d}\n")

# ------------------ Lógica del juego ------------------

def gestionar_jugador(puntajes):
    """
    Solicita un apodo único al jugador y lo registra en el diccionario de puntajes.
    """
    while True:
        apodo = input("Ingresa tu apodo: ").strip()
        if apodo in puntajes:
            print("Ese apodo ya existe, elige otro.")
        else:
            puntajes[apodo] = [0, 0]
            return apodo

def elegir_categoria(categorias):
    """
    Muestra las categorías disponibles y permite al usuario elegir una.
    """
    print("\nCategorías disponibles:")
    for i, cat in enumerate(categorias.keys(), 1):
        print(f"{i}. {cat}")
    while True:
        opcion = input("Elige una categoría: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(categorias):
            return list(categorias.keys())[int(opcion)-1]
        else:
            print("Opción inválida, intenta de nuevo.")

def jugar_partida(categorias, apodo, puntajes):
    """
    Ejecuta una partida del juego del ahorcado con selección de categoría.
    """
    categoria = elegir_categoria(categorias)
    palabra = random.choice(categorias[categoria])
    letras_correctas = []
    letras_incorrectas = []
    intentos = 6

    while intentos > 0:
        estado = [letra if letra in letras_correctas else "_" for letra in palabra]
        print(AHORCADO[6 - intentos])
        print(f"\nCategoría: {categoria}")
        print("Palabra:", " ".join(estado))
        print(f"Intentos restantes: {intentos}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas) if letras_incorrectas else '-'}")

        letra = input("Ingresa una letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa una sola letra válida (a-z).")
            continue

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya intentaste esa letra. Prueba otra.")
            continue

        if letra in palabra:
            letras_correctas.append(letra)
            if all(l in letras_correctas for l in set(palabra)):
                print(f"\n¡Ganaste! La palabra era {palabra}")
                puntajes[apodo][0] += 1
                return
        else:
            letras_incorrectas.append(letra)
            intentos -= 1

    print(f"\nPerdiste. La palabra era {palabra}")
    puntajes[apodo][1] += 1

def mostrar_top_10(puntajes):
    """
    Muestra el ranking de los 10 mejores jugadores según sus victorias.
    """
    ranking = sorted(puntajes.items(), key=lambda x: x[1][0], reverse=True)[:10]
    print("\n--- Top 10 ---")
    for i, (apodo, (v, d)) in enumerate(ranking, 1):
        print(f"{i}. {apodo} - {v} victorias, {d} derrotas")

# ------------------ Menú principal ------------------

def menu():
    """
    Muestra el menú principal del juego y gestiona las opciones del usuario.
    """
    categorias = cargar_palabras()
    puntajes = cargar_puntajes()

    while True:
        print("\n--- AHORCADO ---")
        print("1. Jugar")
        print("2. Ver Top 10")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            apodo = gestionar_jugador(puntajes)
            jugar_partida(categorias, apodo, puntajes)
            guardar_puntajes(puntajes)
        elif opcion == "2":
            mostrar_top_10(puntajes)
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
