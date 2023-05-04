usuarios = [["Chanchito", 4], ["Felipe", 1],
            ["Pulga", 5]]  # map, para transformar
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filter, para filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# map & filter, para transformar y filtrar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
