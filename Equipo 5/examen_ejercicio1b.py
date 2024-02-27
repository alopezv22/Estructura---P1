superficie_inicial=float(input("Ingresa la superficie inicial: "))
numero_generaciones=int(input("Ingresa el numero de generaciones: "))
total_herederos=0
if 0 < numero_generaciones <= 50:
    for i in range (numero_generaciones):
        print(f"Generacion {i+1}")
        numero_herederos=int(input("Ingresa el numero de herederos: "))
        total_herederos+=numero_herederos
else:
    print("No puede haber mas de 50 generaciones y tiene que ser mayor a 0")

print(total_herederos)
print(superficie_inicial/total_herederos)



