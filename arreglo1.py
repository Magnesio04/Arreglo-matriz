import random

materias = ["Español", "Matemáticas", "Física", "Química", "Música", "Inglés"]

matriz_calificaciones = []

for _ in range(100):
    calificaciones_alumno = [random.randint(1, 10) for _ in range(6)]
    matriz_calificaciones.append(calificaciones_alumno)

for i, calificaciones_alumno in enumerate(matriz_calificaciones, start=1):
    if i == 95:
        print(f"\033[1mAlumno {i}: {calificaciones_alumno}\033[0m")  
    else:
        print(f"Alumno {i}: {calificaciones_alumno}")

alumno_buscar = 95
materia_buscar = 5

if 1 <= alumno_buscar <= 100 and 1 <= materia_buscar <= 6:
    calificacion_buscada = matriz_calificaciones[alumno_buscar - 1][materia_buscar - 1]
    print(f"\nCalificación del alumno {alumno_buscar} en {materias[materia_buscar - 1]}: {calificacion_buscada}")
else:
    print("\nÍndices de alumno o materia fuera de rango.")
