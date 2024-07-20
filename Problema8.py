"""
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.

"""
def Factorial(n):
  i=1
  producto=1
  if n==0 or n==1:
     return 1
  else:
     while i<=n:
      producto=i*producto
      i=i+1
  return producto

print(Factorial(4))
    

     
