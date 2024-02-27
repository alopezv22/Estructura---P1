rango = int(input("Ingrese el número de nombres: "))

nombres = []
longitudes = []

for i in range(rango):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)
    longitudes.append(len(nombre))

print("\nnombres y longitudes:")

for hola in range(rango):
    print(f"{nombres[hola]} - longitud: {longitudes[hola]}")
