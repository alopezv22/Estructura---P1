import random

def llenar_vector_aleatorio(longitud):
    return [random.randint(-100, 100) for _ in range(longitud)]

def suma_vectores(vector_a, vector_b):
    return [a + b for a, b in zip(vector_a, vector_b)]

def resta_vectores(vector_a, vector_b):
    return [b - a for a, b in zip(vector_a, vector_b)]

def mostrar_vector(vector, nombre):
    print(f"Vector {nombre}: {vector}")

def validar_longitud(longitud_a, longitud_b):
    return longitud_a == longitud_b

def limpiar_vector(vector):
    return []

def main():
    while True:
        longitud = input("Ingrese la longitud de los vectores (ingrese '0' para salir): ")
        
        try:
            longitud = int(longitud)
            if longitud <= 0:
                if longitud == 0:
                    print("Saliendo del programa...")
                    break
                else:
                    print("La longitud debe ser un número entero positivo mayor que cero.")
                    continue
        except ValueError:
            print("La longitud debe ser un número entero positivo mayor que cero.")
            continue
        
        vector_a = []
        vector_b = []
        vector_c = []
        
        while True:
            print("\nMenu:")
            print("1. Llenar Vector A de manera aleatoria.")
            print("2. Llenar Vector B de manera aleatoria.")
            print("3. Realizar C=A+B")
            print("4. Realizar C=B-A")
            print("5. Mostrar")
            print("6. Limpiar un vector")
            print("7. Salir")
            
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                vector_a = llenar_vector_aleatorio(longitud)
                print("Vector A llenado aleatoriamente.")
            elif opcion == "2":
                vector_b = llenar_vector_aleatorio(longitud)
                print("Vector B llenado aleatoriamente.")
            elif opcion == "3":
                if validar_longitud(len(vector_a), len(vector_b)):
                    vector_c = suma_vectores(vector_a, vector_b)
                    print("Se realizo la suma: C = A + B")
                else:
                    print("Los vectores tienen longitudes diferentes.")
            elif opcion == "4":
                if validar_longitud(len(vector_a), len(vector_b)):
                    vector_c = resta_vectores(vector_b, vector_a)
                    print("Se realizo la resta: C = B - A")
                else:
                    print("Los vectores tienen longitudes diferentes.")
            elif opcion == "5":
                subopcion = input("Seleccione el vector a mostrar (A, B o C): ")
                if subopcion.upper() == "A":
                    mostrar_vector(vector_a, "A")
                elif subopcion.upper() == "B":
                    mostrar_vector(vector_b, "B")
                elif subopcion.upper() == "C":
                    mostrar_vector(vector_c, "C")
                else:
                    print("Opcion no valida.")
            elif opcion == "6":
                subopcion = input("Seleccione el vector a limpiar (A, B o C): ")
                if subopcion.upper() == "A":
                    vector_a = limpiar_vector(vector_a)
                    print("Vector A limpiado.")
                elif subopcion.upper() == "B":
                    vector_b = limpiar_vector(vector_b)
                    print("Vector B limpiado.")
                elif subopcion.upper() == "C":
                    vector_c = limpiar_vector(vector_c)
                    print("Vector C limpiado.")
                else:
                    print("Opcion no valida.")
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion no valida. Por favor, seleccione una opcion valida.")

if __name__ == "__main__":
    main()
