"""
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""
i=1
while i<=5 :
    print("*"*i) 
    i=i+1
while i<=9:
    print("*"*(10-i))
    i=i+1


