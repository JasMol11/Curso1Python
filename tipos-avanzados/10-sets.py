# set significa grupo o  conjunto
# es una coleccion de datos que no se puede repetir y no está ordenada'
# se trabajan similar a las listas
# primer = {1, 1, 2, 2, 3, 4}
# print(primer)

# primer.add(5)
# primer.remove(1)
# print(primer)

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]

segundo = set(segundo)
print(primer)
print(segundo)

# | UNION -> hace una union y elimina los elementos duplicados
print(primer | segundo)

# & INTERCECCION -> muestra los elementos en comun entre los 2 sets
print(primer & segundo)

# - DIFERENCIA -> calcula la diferencia y los eleimina del primer set
print(primer - segundo)

# ^ DIFERENCIA SIMETICA -> devuelve los elementos que se encuentran en el primero y el segundo pero no los que tienen en comun
print(primer ^ segundo)
