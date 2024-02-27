
import random

def llenar_vector(vector, longitud):
 
  for i in range(longitud):
    vector.append(random.randint(-100, 100))

def mostrar_vector(vector):

  for i in range(len(vector)):
    print(f"Vector[{i+1}] = {vector[i]}")

def sumar_vectores(vector_a, vector_b):

  vector_c = []
  for i in range(len(vector_a)):
    vector_c.append(vector_a[i] + vector_b[i])
  return vector_c

def restar_vectores(vector_a, vector_b):

  vector_c = []
  for i in range(len(vector_a)):
    vector_c.append(vector_b[i] - vector_a[i])
  return vector_c

def main():
 
  longitud = int(input("Ingrese la longitud de los vectores: "))

  vector_a = []
  vector_b = []

  llenar_vector(vector_a, longitud)
  llenar_vector(vector_b, longitud)

  
  while True:
    print("\nMenú:")
    print("1. Llenar Vector A de manera aleatoria.")
    print("2. Llenar Vector B de manera aleatoria.")
    print("3. Realizar C=A+B")
    print("4. Realizar C=B-A")
    print("5. Mostrar (Permitiendo al usuario elegir entre el Vector A, B, o C).")
    print("6. Salir.")

    opcion = int(input("Ingrese una opción: "))

  
    if opcion not in range(1, 7):
      print("Opción no válida.")
      continue

 
    if opcion == 1:
      llenar_vector(vector_a, longitud)
      print("Vector A llenado de forma aleatoria.")
    elif opcion == 2:
      llenar_vector(vector_b, longitud)
      print("Vector B llenado de forma aleatoria.")
    elif opcion == 3:
      vector_c = sumar_vectores(vector_a, vector_b)
      print("Vector C = A + B")
    elif opcion == 4:
      vector_c = restar_vectores(vector_b, vector_a)
      print("Vector C = B - A")
    elif opcion == 5:
      opcion_vector = int(input("Ingrese qué vector desea mostrar (1: A, 2: B, 3: C): "))
      if opcion_vector == 1:
        mostrar_vector(vector_a)
      elif opcion_vector == 2:
        mostrar_vector(vector_b)
      elif opcion_vector == 3:
        mostrar_vector(vector_c)
      else:
        print("Opción no válida.")
    else:
     
      break

if __name__ == "__main__":
  main()
