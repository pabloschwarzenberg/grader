#Cálculo del dígito verificador de un rut
rut= int(input("ingrese el rut: "))
primero= (rut%10)*2
segundo= ((rut%100)//10)*3
tercero= ((rut%1000)//100)*4
cuarto= ((rut%10000)//1000)*5
quinto= ((rut%100000)//10000)*6
sexto= ((rut%1000000)//100000)*7
septimo= ((rut%10000000)//1000000)*2
octavo= (rut//10000000)*3
suma=(primero+segundo+tercero+cuarto+quinto+sexto+septimo+octavo)
parte_entera=((suma/11)//1)
resto=suma-(11*parte_entera)
dv=11-resto
if (dv>=1 and dv<=9):
  print("dv=",dv)
elif (dv==10):
  print("dv=K")
elif (dv==11):
  print("dv=0")