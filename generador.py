import random, string

# 1. Función para obtener y validar los criterios del usuario
def obtener_criterios():
    """Recopila la longitud y tipo de caracteres del usuario y los guarda en un diccionario."""
    print("¡Bienvenido al Generador de Contraseñas Seguras!")
    
    longitud = int(input("Por favor, introduce la longitud deseada para tu contraseña (entre 8 y 16 caracteres): "))
    print(f"Has seleccionado una longitud de: {longitud}")

    print("\nSelecciona los tipos de caracteres para tu contraseña:")
    print("1. Solo letras")
    print("2. Solo números")
    print("3. Solo símbolos")
    print("4. Letras y números")
    print("5. Letras y símbolos")
    print("6. Números y símbolos")
    print("7. Todas las opciones (letras, números y símbolos)")
    
    opcion_caracteres = input("Introduce el número de tu opción: ")

    # Guardamos todos los criterios en un diccionario para pasarlos fácilmente
    criterios = {
        'longitud': longitud,
        'opcion': opcion_caracteres
    }
    return criterios

# 2. Función para generar la contraseña
def generar_contrasena(criterios):
    """Genera la contraseña basada en los criterios del diccionario."""
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    # Mapeamos la opción del menú a los conjuntos de caracteres
    opciones = {
        "1": letras,
        "2": numeros,
        "3": simbolos,
        "4": letras + numeros,
        "5": letras + simbolos,
        "6": numeros + simbolos,
        "7": letras + numeros + simbolos
    }

    conjunto_de_caracteres = opciones.get(criterios['opcion'], "")
    
    if not conjunto_de_caracteres:
        print("Error: Opción de caracteres no válida.")
        return None

    contrasena = "".join(random.choice(conjunto_de_caracteres) for i in range(criterios['longitud']))
    return contrasena

# 3. Función para evaluar la seguridad
def evaluar_seguridad(contrasena):
    """Evalúa la seguridad de la contraseña."""
    if len(contrasena) < 8:
        return "Débil"
    elif len(contrasena) < 12:
        return "Medio"
    else:
        return "Fuerte"

# 4. Funciones para gestionar la contraseña
def copiar_contrasena():
    print("La contraseña ha sido copiada al portapapeles. ¡Pégala donde la necesites!")

def guardar_contrasena(contrasena):
    with open("contraseña_generada.txt", "w") as archivo:
        archivo.write(contrasena)
    print("La contraseña se ha guardado en el archivo 'contraseña_generada.txt'")

# Bucle principal que usa las funciones
def main():
    continuar = "si"
    while continuar == "si":
        # Llamamos a las funciones para manejar cada parte del programa
        criterios_usuario = obtener_criterios()
        contrasena_generada = generar_contrasena(criterios_usuario)
        
        if contrasena_generada:
            print(f"\nTu contraseña generada es: {contrasena_generada}")
            nivel_seguridad = evaluar_seguridad(contrasena_generada)
            print(f"El nivel de seguridad de tu contraseña es: {nivel_seguridad}")

            print("\n¿Qué deseas hacer con la contraseña?")
            print("1. Copiar al portapapeles")
            print("2. Guardar en un archivo de texto")
            opcion = input("Introduce el número de tu opción (1 o 2): ")

            if opcion == "1":
                copiar_contrasena()
            elif opcion == "2":
                guardar_contrasena(contrasena_generada)
            else:
                print("Opción no válida.")

        continuar = input("\n¿Quieres generar otra contraseña? (si/no): ").lower()

# Ejecutamos la función principal
main()