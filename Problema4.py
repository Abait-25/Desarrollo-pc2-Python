"""
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
"""
alumnos = []
n = int(input("¿Cuántos alumnos desea ingresar? "))
for _ in range(n):
    nombre = input("Ingrese el nombre del alumno: ")
    
    calificaciones = []
    for i in range(3):
        while True:
            cadena_nota = input(f"Ingrese la calificación {i+1} del alumno {nombre}: ")
            
            if cadena_nota.replace('.', '', 1).isdigit() and cadena_nota.count('.') <= 1:
                nota = float(cadena_nota)
                calificaciones.append(nota)
                break
            else:
                print("Por favor, ingrese un número válido para la calificación.")
    
    alumnos.append({
        "Alumno": nombre,
        "Notas": calificaciones
    })

print("\nListado completo de alumnos:")
for alumno in alumnos:
    nombre = alumno["Alumno"]
    notas = alumno["Notas"]
    print(f"Alumno: {nombre}, Notas: {notas}")
