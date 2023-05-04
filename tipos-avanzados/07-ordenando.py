numeros = [4, 6, 7, 8, 5, 3, 2]

numeros.sort()
print(numeros)

# aqui si afecta la lista original
numeros.sort(reverse=True)
print(numeros)

# devuelve una nueva lista, no afecta la lista original
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
usuarios.sort()
print(usuarios)

usuarios2 = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


def ordena(elemento):
    return elemento[1]


usuarios2.sort(key=ordena)
print(usuarios)

usuarios2.sort(key=lambda el: el[1], reverse=True)
print(usuarios2)
