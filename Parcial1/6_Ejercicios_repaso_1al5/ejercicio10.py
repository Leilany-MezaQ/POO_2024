def contar_aprobados_reprobados():
    aprobados = 0
    reprobados = 0

    for _ in range(15):
        calificacion = float(input("Introduce la calificación del alumno: "))
        if calificacion >= 6:
            aprobados += 1
        else:
            reprobados += 1

    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")

contar_aprobados_reprobados()







