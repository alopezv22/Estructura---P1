import random

class Vectores:
    def __init__(self, tamaño_vector):
        self.tamaño_vector = int(tamaño_vector)
        self.vectorA = []
        self.vectorB = []
        self.vectorC = []

    def llenar_vector_A(self):
        self.vectorA = [random.randint(-100, 100) for _ in range(self.tamaño_vector)]
        return self.vectorA

    def llenar_vector_B(self):
        self.vectorB = [random.randint(-100, 100) for _ in range(self.tamaño_vector)]
        return self.vectorB

    def suma_vectores(self):
        self.vectorC = [a + b for a, b in zip(self.vectorA, self.vectorB)]
        return self.vectorC

    def resta_vectores(self):
        self.vectorC = [b - a for a, b in zip(self.vectorA, self.vectorB)]
        return self.vectorC

    def validar_operacion(self, operacion):
        if len(self.vectorC) == self.tamaño_vector:
            print(f"La operación de {operacion} de vectores se realizó correctamente.")
        else:
            print(f"Error: La operación de {operacion} de vectores no se realizó correctamente.")

    def mostrar_vectores(self, opcion):
        if opcion == 'a':
            print("Vector A:", self.vectorA)
        elif opcion == 'b':
            print("Vector B:", self.vectorB)
        elif opcion == 'c':
            print("Vector C:", self.vectorC)

print("Bienvenido\n")
n = input("Introduce el tamaño de los vectores que deseas generar: \n")
vectores = Vectores(n)

vectores_generados = False

while True:
    print("\nElige el número de la opción que deseas realizar:")
    print("1. GENERAR VECTOR A")
    print("2. GENERAR VECTOR B")
    print("3. REALIZAR C = A + B")
    print("4. REALIZAR C = B - A")
    print("5. MOSTRAR VECTORES")
    print("6. SALIR")

    opcion = input(">> ")

    if opcion == '1':
        vectores.llenar_vector_A()
        print("Vector A generado.")
        vectores_generados = True

    elif opcion == '2':
        vectores.llenar_vector_B()
        print("Vector B generado.")
        vectores_generados = True

    elif opcion == '3':
        if not vectores_generados:
            print("No se ha generado ningún vector. Por favor, genere al menos un vector primero.")
        else:
            vectores.suma_vectores()
            print("Se ha realizado C = A + B.")
            vectores.validar_operacion('suma')
            vectores.mostrar_vectores('c')

    elif opcion == '4':
        if not vectores_generados:
            print("No se ha generado ningún vector. Por favor, genere al menos un vector primero.")
        else:
            vectores.resta_vectores()
            print("Se ha realizado C = B - A.")
            vectores.validar_operacion('resta')
            vectores.mostrar_vectores('c')

    elif opcion == '5':
        if not vectores_generados:
            print("No se ha generado ningún vector. Por favor, genere al menos un vector primero.")
        else:
            opcion_vectores = input("¿Qué vector deseas mostrar (a, b, c)? ")
            vectores.mostrar_vectores(opcion_vectores)

    elif opcion == '6':
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")






