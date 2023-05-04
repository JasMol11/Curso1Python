# son una conexion de daros que se agrupan por llaves y un valor
# lo de la izquierda SIEMPRE UN STRING
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

# print(punto, punto["lala"])
if "lala" in punto:
    print("Encontré Lala", punto["lala"])


print(punto.get("x"))
print(punto.get("lala", "No lo encontré pai"))


# del punto["x"]
# del (punto["y"])
# print(punto)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
