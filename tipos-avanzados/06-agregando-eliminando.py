mascotas = [
    "wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito Feliz"
]
print(mascotas)
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito Triste")
print(mascotas)

# aqui no va el indice, va a el elemento que queremos eliminar, solo elimina el primero
mascotas. remove("Pulga")
print(mascotas)

# elimina el ultimo elemento, si agregamos el indice elimina ese
mascotas.pop(1)
print(mascotas)

del mascotas[0]
print(mascotas)

mascotas.clear()
print(mascotas)
