#Descomponer un número
numero=int(input("Ingrese un numero: "))

mil=(numero//1000)
centena=(numero//100 - mil*10)
decena=(numero//10 - mil*100 - centena*10)
unidad=(numero - mil*1000 - centena*100 - decena*10)

Mil=str(mil)
Centena=str(centena)
Decena=str(decena)
Unidad=str(unidad)

if mil>0:
    print(Mil + "M + "+ Centena + "C + " + Decena + "D + " + Unidad + "U")
if mil==0 and centena>0:
    print(Centena + "C + " + Decena + "D + " + Unidad + "U")
if mil==0 and centena==0 and decena>0:
    print(Decena + "D + " + Unidad + "U")
if mil==0 and centena==0 and decena==0:
    print(Unidad + "U")