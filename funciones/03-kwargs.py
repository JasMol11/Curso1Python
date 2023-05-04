# se agregan los 2** para convertirlo en un key word argument, para agregar diversos parametros
def get_product(**datos):
    # [con comillas doble se agrega el nombre del parametro al que queremos acceder]
    print(datos["id"], datos["name"])


get_product(id="11",
            name="iPhone",
            desc="Esto es un iPhone")
# basicamente es para crear diccionarios de datos, agregamos el nombre del parametro y luego su valor
