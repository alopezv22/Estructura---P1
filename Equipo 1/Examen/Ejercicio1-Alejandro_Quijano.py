

def calcular_superficie_terreno(superficie_inicial, numb_generaciones, numb_herederos):
  superficies = [[0] * numb_herederos for _ in range(numb_generaciones)]

  superficies[0] = [superficie_inicial / numb_herederos] * numb_herederos

  for generacion in range(1, numb_generaciones):
      for heredero in range(numb_herederos):
          superficie_por_heredero = superficies[generacion - 1][heredero] / numb_herederos
          superficies[generacion][heredero] = superficie_por_heredero

  superficie_final = sum(superficies[-1])
  return superficie_final

def main():
  superficie_inicial = float(input("Ingrese la superficie inicial del terreno: "))
  numb_generaciones = int(input("Ingrese el número de generaciones: "))
  numb_herederos = int(input("Ingrese el número de herederos por generación: "))

  if numb_generaciones > 50:
      print("El número máximo de generaciones es 50. Se ajustará automáticamente.")
      numb_generaciones = 50

  superficie_final = calcular_superficie_terreno(superficie_inicial, numb_generaciones, numb_herederos)
  print(f"Superficie final del terreno para el heredero: {superficie_final}")

main()
