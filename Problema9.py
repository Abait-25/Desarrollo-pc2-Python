"""
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?
"""
texto_usuario = input("Ingresa una cadena de texto: ")
vocales = "aeiouAEIOU"
resultado = ""
for caracter in texto_usuario:
    if caracter not in vocales:
        resultado += caracter

print("Texto sin vocales:", resultado)