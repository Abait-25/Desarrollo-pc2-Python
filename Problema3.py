"""
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO
Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4
"""

lista=[]
respuesta="SI"
while respuesta=="SI" :
 respuesta=input("Desea ingresar un número? ")
 if respuesta=="SI":
    numero=int(input("Ingrese el número: "))
    lista.append(numero)

 elif respuesta=="NO":
    break 
print(lista)

n=0
m=0
for i in lista:
  if(i %2==0):
    n=n+1
  else:
    m=m+1

print(f" Cantidad de números pares: {n}")
print(f" Cantidad de números impares: {m}")





