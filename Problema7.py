"""
Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
(excluyendo el propio número).
Ejemplo Identificar número perfecto:
Número perfecto: 6
● Divisores propios: 1, 2, 3
● Suma de los divisores propios: 1 + 2 + 3 = 6

"""
def es_numero_perfecto(num):
    divisores = [i for i in range(1, num) if num % i == 0]
    return sum(divisores) == num

def encontrar_numeros_perfectos(hasta):
    numerosPerfectos = []
    for num in range(1, hasta):
        if es_numero_perfecto(num):
            numerosPerfectos.append(num)
    return numerosPerfectos


numeros_perfectos_menores_1000 = encontrar_numeros_perfectos(1000)

print("Números perfectos menores que 1000:", numeros_perfectos_menores_1000)