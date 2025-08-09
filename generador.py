import random, string

print("¡Bienvenido al Generador de Contraseñas Seguras!")

# Bucle principal para que el programa se repita hasta que el usuario decida salir
continuar = "si"
while continuar == "si":
    # Le indicamos al usuario el rango de longitud
    longitud = int(input("Por favor, introduce la longitud deseada para tu contraseña (entre 8 y 16 caracteres): "))
    print(f"Has seleccionado una longitud de: {longitud}")
    
    # Nuevo menú de opciones para los tipos de caracteres
    print("\nSelecciona los tipos de caracteres para tu contraseña:")
    print("1. Solo letras")
    print("2. Solo números")
    print("3. Solo símbolos")
    print("4. Letras y números")
    print("5. Letras y símbolos")
    print("6. Números y símbolos")
    print("7. Todas las opciones (letras, números y símbolos)")
    
    opcion_caracteres = input("Introduce el número de tu opción: ")

    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    conjunto_de_caracteres = ""
    # Nueva lógica para construir el conjunto de caracteres basado en la opción del menú
    if opcion_caracteres == "1":
        conjunto_de_caracteres = letras_minusculas + letras_mayusculas
    elif opcion_caracteres == "2":
        conjunto_de_caracteres = numeros
    elif opcion_caracteres == "3":
        conjunto_de_caracteres = simbolos
    elif opcion_caracteres == "4":
        conjunto_de_caracteres = letras_minusculas + letras_mayusculas + numeros
    elif opcion_caracteres == "5":
        conjunto_de_caracteres = letras_minusculas + letras_mayusculas + simbolos
    elif opcion_caracteres == "6":
        conjunto_de_caracteres = numeros + simbolos
    elif opcion_caracteres == "7":
        conjunto_de_caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos
    else:
        print("Error: Opción de caracteres no válida.")
        
    if not conjunto_de_caracteres:
        print("No se ha podido generar la contraseña.")
    else:
        contrasena = "".join(random.choice(conjunto_de_caracteres) for i in range(longitud))
        print(f"\nTu contraseña generada es: {contrasena}")

        # La siguiente lógica evalúa el nivel de seguridad de la contraseña
        if longitud < 8:
            print("El nivel de seguridad de tu contraseña es: Débil")
        elif longitud < 12:
            print("El nivel de seguridad de tu contraseña es: Medio")
        else:
            print("El nivel de seguridad de tu contraseña es: Fuerte")

        print("\n¿Qué deseas hacer con la contraseña?")
        print("1. Copiar al portapapeles")
        print("2. Guardar en un archivo de texto")
        opcion = input("Introduce el número de tu opción (1 o 2): ")

        if opcion == "1":
            print("La contraseña ha sido copiada al portapapeles. ¡Pégala donde la necesites!")
        elif opcion == "2":
            with open("contraseña_generada.txt", "w") as archivo:
                archivo.write(contrasena)
            print("La contraseña se ha guardado en el archivo 'contraseña_generada.txt'")
        else:
            print("Opción no válida. Por favor, reinicia el programa.")
    
    # Esta línea pregunta si continuar y controla el bucle.
    continuar = input("\n¿Quieres generar otra contraseña? (si/no): ").lower()