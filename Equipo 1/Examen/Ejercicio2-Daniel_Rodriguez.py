def ingresar_nombres_y_longitudes():
  n = int(input("Ingrese la cantidad de nombres que desea ingresar: "))
  nombres = []
  longitudes = []
  for i in range(n):
      nombre = input("Ingrese el nombre {}: ".format(i+1))
      nombres.append(nombre)
      longitudes.append(len(nombre))
  return nombres, longitudes

def mostrar_nombres_y_longitudes(nombres, longitudes):
  print("\nNombres y sus longitudes:")
  for nombre, longitud in zip(nombres, longitudes):
      print("Nombre: {}, Longitud: {}".format(nombre, longitud))

nombres, longitudes = ingresar_nombres_y_longitudes()

mostrar_nombres_y_longitudes(nombres, longitudes)