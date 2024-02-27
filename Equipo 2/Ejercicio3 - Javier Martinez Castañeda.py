alumnos_estructura = []
numero_alumnos_estructura = int(input("¿Cuántos alumnos hay en Estructura? "))
for i in range(numero_alumnos_estructura):
    alumno = int(input("ID del alumno {}: ".format(i + 1)))
    alumnos_estructura.append(alumno)
alumnos_programacion = []
numero_alumnos_programacion = int(input("¿Cuántos alumnos hay en Programación? "))
for i in range(numero_alumnos_programacion):
    alumno = int(input("ID del alumno {}: ".format(i + 1)))
    alumnos_programacion.append(alumno)
alumnos_comunes = []
for alumno in alumnos_estructura:
    if alumno in alumnos_programacion:
        alumnos_comunes.append(alumno)
numero_alumnos_comunes = len(alumnos_comunes)
print("Alumnos comunes en Estructura y Programación:")
for i in range(numero_alumnos_comunes):
    print("{} - {}".format(i + 1, alumnos_comunes[i]))
print("Número total de alumnos comunes:", numero_alumnos_comunes)
