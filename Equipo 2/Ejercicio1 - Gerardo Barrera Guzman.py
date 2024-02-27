def calcular_superficie(superficie_inicial, generaciones, herederos_por_generacion):
    superficie_actual = superficie_inicial

    for generacion in range(generaciones):
        print(f"Generación {generacion}: Superficie = {superficie_actual:.2f}")
        superficie_actual /= herederos_por_generacion

    return superficie_actual

def main():
    try:
        superficie_inicial = float(input("Ingrese la superficie inicial del terreno: "))
        generaciones = int(input("Ingrese el número de generaciones (máximo 50): "))
        herederos_por_generacion = int(input("Ingrese el número de herederos por generación: "))

        if generaciones <= 0 or generaciones > 50:
            print("El número de generaciones debe estar entre 1 y 50.")
            return

        if herederos_por_generacion <= 0:
            print("El número de herederos por generación debe ser mayor que cero.")
            return

        resultado = calcular_superficie(superficie_inicial, generaciones, herederos_por_generacion)
        print(f"\nSuperficie final después de {generaciones} generaciones: {resultado:.2f}")

    except ValueError:
        print("Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
