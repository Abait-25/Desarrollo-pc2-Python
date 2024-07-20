"""
Escribe un programa que encuentre la suma de todos los números primos menores que 100.

"""
def es_primo(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_primos(menor_que):

    suma = 0
    for num in range(2, menor_que):
        if es_primo(num):
            suma += num
    return suma

resultado = suma_primos(100)
print(f"La suma de todos los números primos menores que 100 es: {resultado}")