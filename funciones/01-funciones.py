# def hola():  palabra def, seguido del nombre de lla funcion, () :
#    print("Hola Mundo")
#    print("Ultimate Python")


# hola()


# def hola(nombre, apellido):  # aqui es un parametro, es el nombre de la variable dentro de la funcion
#     print("Hola Mundo")
#     print(f"Bienvenido {nombre} {apellido} :)")  # {aqui es un parametro}


# # pero aqui cuando se le asigna, ya se convierte en un argumento
# hola("Jason", "Molina")
# hola("Chanchito", "Feliz")


# es para que utilice parametros de manera opcional, asignamos un valor por defecto al parametro
def hola(nombre, apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido} :)")


hola("Jason", "Molina")
hola("Chanchito")


hola(apellido="Peraza", nombre="Jonathan")
