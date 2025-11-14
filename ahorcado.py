import random
import os

# ------------------ Manejo de archivos ------------------

def cargar_palabras(ruta="palabras.txt"):
    """Lee palabras.txt y devuelve una lista de palabras."""
    if not os.path.exists(ruta):
        print("No se encontró palabras.txt")
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return [linea.strip().lower() for linea in f if linea.strip()]

def cargar_puntajes(ruta="puntajes.txt"):
    """Lee puntajes.txt y devuelve un diccionario {apodo: [victorias, derrotas]}."""
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
    """Escribe puntajes en puntajes.txt."""
    with open(ruta, "w", encoding="utf-8") as f:
        for apodo, (v, d) in puntajes.items():
            f.write(f"{apodo},{v},{d}\n")

# ------------------ Lógica del juego ------------------

def gestionar_jugador(puntajes):
    """Pide un apodo único al usuario."""
    while True:
        apodo = input("Ingresa tu apodo: ").strip()
        if apodo in puntajes:
            print("Ese apodo ya existe, elige otro.")
        else:
            puntajes[apodo] = [0, 0]  # victorias, derrotas
            return apodo

def jugar_partida(palabras, apodo, puntajes):
    """Ejecuta una partida del ahorcado."""
    palabra = random.choice(palabras)
    letras_correctas = []
    letras_incorrectas = []
    intentos = 6

    while intentos > 0:
        # Mostrar estado actual
        estado = [letra if letra in letras_correctas else "_" for letra in palabra]
        print("\nPalabra:", " ".join(estado))
        print(f"Intentos restantes: {intentos}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas) if letras_incorrectas else '-'}")

        letra = input("Ingresa una letra: ").lower().strip()

        # Validación de entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa una sola letra válida (a-z).")
            continue

        # Verificar si ya fue intentada
        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya intentaste esa letra. Prueba otra.")
            continue

        # Verificar si la letra está en la palabra
        if letra in palabra:
            letras_correctas.append(letra)
            if all(l in letras_correctas for l in set(palabra)):
                print(f"\n¡Ganaste! La palabra era {palabra}")
                puntajes[apodo][0] += 1
                return
        else:
            letras_incorrectas.append(letra)
            intentos -= 1

    # Si se acaban los intentos
    print(f"\nPerdiste. La palabra era {palabra}")
    puntajes[apodo][1] += 1

def mostrar_top_10(puntajes):
    """Muestra el ranking Top 10 por victorias."""
    ranking = sorted(puntajes.items(), key=lambda x: x[1][0], reverse=True)[:10]
    print("\n--- Top 10 ---")
    for i, (apodo, (v, d)) in enumerate(ranking, 1):
        print(f"{i}. {apodo} - {v} victorias, {d} derrotas")

# ------------------ Menú principal ------------------

def menu():
    palabras = cargar_palabras()
    puntajes = cargar_puntajes()

    while True:
        print("\n--- AHORCADO ---")
        print("1. Jugar")
        print("2. Ver Top 10")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            apodo = gestionar_jugador(puntajes)
            jugar_partida(palabras, apodo, puntajes)
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