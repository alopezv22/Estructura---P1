def encontrar_alumnos_comunes(estructura, programacion):
    alumnos_comunes = []
    for id_estructura in estructura:
        for id_programacion in programacion:
            if id_estructura == id_programacion:
                alumnos_comunes.append(id_estructura)
    return alumnos_comunes

estructura = [1, 2, 3, 4, 5, 6, 7, 8, 9]
programacion = [2, 3, 4, 6, 7, 8, 9, 11, 12]

alumnos_comunes = encontrar_alumnos_comunes(estructura, programacion)

print(f"Numero de repeticiones: {len(alumnos_comunes)}")
