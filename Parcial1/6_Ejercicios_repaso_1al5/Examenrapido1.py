
MATERIAS = 3

alumnos = []
while True:
    nombre = input("Nombre del alumno: ")
    carrera = input("Carrera: ")

    calificaciones = []
    for i in range(MATERIAS):
        calificacion = float(input(f"Calificación {i + 1}: "))
        calificaciones.append(calificacion)

    promedio_parciales = sum(calificaciones) / MATERIAS
 
    calificacion_proyecto = float(input("Calificación del proyecto final: "))

    calificacion_final = (promedio_parciales + calificacion_proyecto) / 2

    if calificacion_final < 80 or calificacion_proyecto > 50:
        leyenda = "Presenta examen extraordinario"
    else:
        leyenda = "No presenta examen extraordinario"

    alumnos.append((nombre, carrera, calificacion_final, leyenda))

    respuesta = input("¿Desea otra captura? (si/no): ")
    if respuesta.lower() != "si":
        break

promedio_calificaciones_finales = sum(alumno[2] for alumno in alumnos) / len(alumnos)

print("\n***** Resultados *****")
for nombre, carrera, calificacion_final, leyenda in alumnos:
    print(f"Alumno: {nombre} | Carrera: {carrera}")
    print(f"Calificación final: {calificacion_final:.2f} | {leyenda}\n")

print(f"Promedio de calificaciones finales: {promedio_calificaciones_finales:.2f}")





