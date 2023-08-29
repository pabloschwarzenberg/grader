#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut: "))
print("descomponer rut",rut//10000000)
print("descomponer rut",rut//1000000)
print("descomponer rut",rut//100000)
print("descomponer rut",rut//10000)
print("descomponer rut",rut//1000)
print("descomponer rut",rut//100)
print("descomponer rut",rut//10)
print("descomponer rut",rut//1)
d1=(rut//10000000)*3
print("digito 1: ",d1)
d2=((rut//1000000)%10)*2
print("digito 2: ",d2)
d3=((rut//100000)%10)*7
print("digito 3: ",d3)
d4=((rut//10000)%10)*6
print("digito 4: ",d4)
d5=((rut//1000)%10)*5
print("digito 5: ",d5)
d6=((rut//100)%10)*4
print("digito 6: ",d6)
d7=((rut//10)%10)*3
print("digito 7: ",d7)
d8=((rut//1)%10)*2
suma=(d1+d2+d3+d4+d5+d6+d7+d8)
print("Total: ",suma)
resto=suma//11
print("Resto=suma//11",resto)
resto1=suma-(11*resto)
print("Total de resto1=suma-(11*resto)",resto1)
sustraccion=11-resto1
print("Total de la sustraccion=11-resto1: ",sustraccion)
if sustraccion == 11:
    print("dv=",end="")
    print(0)
if sustraccion == 10:
    print("dv=",end="")
    print("K")
else:
    print("dv=",end="")
    print(sustraccion)      