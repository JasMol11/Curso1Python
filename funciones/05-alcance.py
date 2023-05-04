# si se agrega aqui, tiene alcance global, podrá ser accesida por todo el codigo
# usar variables globales es una mala práctica xd
# saludo = "Hola Global"


def saludar():
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)

# aunque ambas se llaman igual, son completamente distintas


saludar()
saludaChanchito()
