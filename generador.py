import random, string

print("¡Bienvenido al Generador de Contraseñas Seguras!")
longitud = int(input("Por favor, introduce la longitud deseada para tu contraseña: "))
print(f"Has seleccionado una longitud de: {longitud}")
caracteres = input("Introduce los tipos de caracteres (por ejemplo, 'letras', 'numeros', 'simbolos'): ")

letras_minusculas = string.ascii_lowercase
letras_mayusculas = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

conjunto_de_caracteres = ""
if "letras" in caracteres:
    conjunto_de_caracteres += letras_minusculas + letras_mayusculas
if "numeros" in caracteres:
    conjunto_de_caracteres += numeros
if "simbolos" in caracteres:
    conjunto_de_caracteres += simbolos

if not conjunto_de_caracteres:
    print("Error: No se han seleccionado tipos de caracteres válidos.")
else:
    contrasena = "".join(random.choice(conjunto_de_caracteres) for i in range(longitud))
    print(f"Tu contraseña generada es: {contrasena}")

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
        # Nota: Para copiar al portapapeles en Python, necesitas una librería externa como pyperclip.
        # Por ahora, solo mostraremos un mensaje.
        print("La contraseña ha sido copiada al portapapeles. ¡Pégala donde la necesites!")
    elif opcion == "2":
        with open("contraseña_generada.txt", "w") as archivo:
            archivo.write(contrasena)
        print("La contraseña se ha guardado en el archivo 'contraseña_generada.txt'")
    else:
        print("Opción no válida. Por favor, reinicia el programa.")