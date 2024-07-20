"""
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.

"""
def fibonacci_hasta_50():
    
    serie = []
    a, b = 0, 1
    
    while a <= 50:
        serie.append(a)
        a, b = b, a + b
        
    return serie

fibonacci_serie = fibonacci_hasta_50()
print("Serie de Fibonacci entre 0 y 50:", fibonacci_serie)