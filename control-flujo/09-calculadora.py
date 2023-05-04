print("Bienvenidos a la calculadora")
print("Para salir, escribe \"salir\"")
print("La operaciones son \"suma, resta, multi y div\"")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("Ingresa la operación que deseas ejecutar: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2

    elif op.lower() == "resta":
        resultado -= n2

    elif op.lower() == "multi":
        resultado *= n2

    elif op.lower() == "div":
        resultado /= n2

    else:
        print("Operación no válida")
        break

    print(f"El resultado es {resultado}")
