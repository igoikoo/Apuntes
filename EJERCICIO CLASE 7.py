lista_nombre = []
while True:
    nombre = input("Nombre:")
    if nombre == "fin":
        break
    telefono = input("Telefono:")
    linea = {}
    linea["Nombre"] = nombre
    linea["Telefono"] = telefono
    lista_nombre.append(linea)