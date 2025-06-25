usuarios =[]

def agregar_usuario(nombre, sexo, contraseña):
    usuario = {"nombre": nombre, "sexo": sexo, "contraseña": contraseña}
    usuarios.append(usuario)
    print(f"usuario agregado: {nombre}")

def buscar_usuario(nombre):
    for usuario in usuarios:
        if usuario ["nombre"] == nombre:
            print(f"usuario encontrado el sexo del usuario es: {sexo} y la contraseña es: {contraseña}")
            return
    print("el usuario no existe")

def eliminar_usuario(nombre):
    for usuario in usuarios:
        if usuario ["nombre"] == nombre:
            usuarios.remove(usuario)
            print("usuario eliminado con exito!")
            return
    print("no se encontro el usuario")
        


while True:

    print("****MENU PRINCIPAL****")
    print("1.-ingresar usuario")
    print("2.-buscar usuario")
    print("3.-eliminar usuario")
    print("4.-salir")

    opcion = input("ingrese una opcion: ")

    if opcion == "1":
        nombre = input("ingrese nombre de usuario: ")
        sexo = input("ingrese sexo: ")
        contraseña = input("ingresecontraseña: ")

        agregar_usuario(nombre, sexo, contraseña)
        
    if opcion == "2":
        input("ingrese el nombre del usuario: ")
        buscar_usuario(nombre)

    if opcion == "3":
        input("ingree el nombre del usuario: ")
        eliminar_usuario(nombre)


    elif opcion == "4":
        break

    else:
        print("opcion no valida, intente de nuevo")
