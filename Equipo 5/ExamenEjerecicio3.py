def Alumnoscomunes(estructura, programacion):
    alumnoscomunes = []
    repeticiones = 0

    for IDEstructura in estructura:
        if IDEstructura in programacion and IDEstructura not in alumnoscomunes:
            alumnoscomunes.append(IDEstructura)
            repeticiones += 1
    
    return alumnoscomunes, repeticiones

IDEstructura = []
IDProgramacion = []

print("Escriba las matriculas recordar que la Matricula es de 5 numeros y que son solo numeros. Ejemplo: 54123")
print("Escriba los IDs de los alumnos de Estructura:")
for i in range(1, 6):
    IDEstructura.append(int(input("ID de estudiante {}: ".format(i))))

print("Escriba los IDs de los alumnos de Programación:")
for i in range(1, 6):
    IDProgramacion.append(int(input("ID de estudiante {}: ".format(i))))

alumnoscomunes, repeticiones = Alumnoscomunes(IDEstructura, IDProgramacion)

print("Los IDs de los alumnos comunes son:", alumnoscomunes)
print("El número de alumnos comunes es:", repeticiones)
