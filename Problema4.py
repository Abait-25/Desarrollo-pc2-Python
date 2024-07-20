# Lista de diccionarios con información de alumnos
alumnos = [
    {"Nombre": "Juan", "Notas": [10, 12, 15]},
    {"Nombre": "Ana", "Notas": [8, 9, 10]},
    {"Nombre": "Carlos", "Notas": [7, 8, 9]}
]

# Calcular y mostrar el promedio de notas de cada alumno
for alumno in alumnos:
    promedio = sum(alumno["Notas"]) / len(alumno["Notas"])
    print(alumno)
    print(f"Nombre: {alumno['Nombre']}, Promedio: {promedio:.2f}")