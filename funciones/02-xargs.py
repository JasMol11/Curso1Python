def suma(*numeros):  # convierte en iterable a la variable, así podemos aplicar un FOR
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 7)
suma(2, 8, 7, 45, 32)
