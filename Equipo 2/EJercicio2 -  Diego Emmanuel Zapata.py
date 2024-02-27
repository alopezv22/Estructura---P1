tamano = int(input("Digite el tamaño de los arreglos: "))
nombres = []
longitudes = []

for i in range(tamano):
    nombre = input("Digite el nombre {}: ".format(i + 1))
    nombres.append(nombre)

for nombre in nombres:
    longitud = len(nombre)
    longitudes.append(longitud)

for i in range(tamano):
    print("Nombre {}: {}".format(i + 1, nombres[i]))
    print("Longitud {}: {}".format(i + 1, longitudes[i]))
    print()

