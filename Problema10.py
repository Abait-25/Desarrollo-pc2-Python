"""
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
Ejemplos:
- Input: 9/8/1636 | Output: 1636-09-08
- Input: Septiembre 8, 1636 | Output: 1636-09-08
- Input: 1/1/1970 | Output: 1970-01-01
"""
fecha_a=input("Digite fecha en formato MES/DIA/AÑO :  ")
if "," in fecha_a:
   parteFecha,año=fecha_a.split(",",1)
   mes,dia=parteFecha.split(" ",1)
   año=año.strip()
   Nombre_meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
   for i in range (0,11):
     if Nombre_meses[i]==mes:
        mes=i+1
   print(f" {año}-{mes:02d}-{dia:02d}")
else:
    # Formato "DÍA/MES/AÑO"
    dia, mes, año = fecha_a.split("/")
    # Convertir a enteros para asegurar el formato
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    print(f"{año}-{mes:02d}-{dia:02d}")

 
 
