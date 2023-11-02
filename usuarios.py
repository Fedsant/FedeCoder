import json

base_de_dato = open("usuarios.txt", "w")

usuarios = {}

def registrar_usuario():
    usuario = input("Ingresar su Usuario: ")
    clave = input("Ingrese su clave: ")
    usuarios[usuario] = clave
    guardar_en_archivo()
    print("USUARIO REGISTRADO.")

def guardar_en_archivo():
    with open("usuarios.txt", "w") as archivo:
        for usuario, clave in usuarios.items():
            archivo.write(f"{usuario}:{clave}\n")

base_de_dato.close()

def mostrar_informacion():
    print("Lista de usuarios registrados: ")
    for usuario in usuarios:
        print(usuario)

def login_usuario():
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese la Clave: ")
    if usuario in usuarios and usuarios[usuario] == clave:
        print("BIENVENIDO")
    else:
        print("Usuario o clave incorrecta. Sino registrese.")

try:
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            usuario, clave = linea.strip().split(":")
            usuarios[usuario] = clave
except ValueError:
    pass

while True:
    print("\n1. Registrar Usuario.")
    print("2. Iniciar sesion.")
    print("3. Mostrar usuarios registrados.")
    print("4. Salir.")

    menu = input("seleccione una opcion: ")

    if menu == "1":
        registrar_usuario()
    elif menu == "2":
        login_usuario()
    elif menu == "3":
        mostrar_informacion()
    elif menu == "4":
        break
    else:
        print("opcion no valida. INTENTE DE NUEVO")