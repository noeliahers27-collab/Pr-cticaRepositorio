# Curso: Fundamentos de Tecnologías Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Noelia M Hernández S.

def ejecutar_programa():
    print("=" * 40)
    print("---BIENVENIDO AL PROGRAMA NOELIA---")
    print("=" * 40)

    nombre = input("¿Como te llamas?")
    color = input("¿Cual es tu color favorito?")
    print("\n" + "-" * 40)
    print(f"¡Hola, {nombre} voy a analizar tus datos...")
    print("-" * 40)

    if color.lower()== "azul":
        print(f"{nombre}, tienes una personalidad calmada y analítica, además se sabe que sientes mucho amor hacía tus cercanos.")
    elif color.lower()== "rojo":
        print(f"{nombre}, tienes una personalidad llena de energía y pasión, hacés faliz a los que te rodean")
    else:
        print(f"¡Que gran elección, el color {color}, tambien es mi favorito y te representa muy bien, {nombre}")

    print("-" * 40)
    print("¡Gracias por su participación¡")
    print("-" * 40)
    
ejecutar_programa()
