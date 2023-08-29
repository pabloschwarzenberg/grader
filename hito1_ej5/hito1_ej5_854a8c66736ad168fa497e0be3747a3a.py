#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese un rut sin digito verificador: "))
while not (rut>=1000000 and rut<=99999999):
    rut=int(input("Ingrese un rut valido: "))
rutTexto=str(rut)
if (rut>=1000000 and rut<=9999999):
    primerDigito=0
else:
    primerDigito=int(rutTexto[7:8])
segundoDigito=int(rutTexto[6:7])
tercerDigito=int(rutTexto[5:6])
cuartoDigito=int(rutTexto[4:5])
quintoDigito=int(rutTexto[3:4])
sextoDigito=int(rutTexto[2:3])
septimoDigito=int(rutTexto[1:2])
octavoDigito=int(rutTexto[0:1])
if (rut>=1000000 and rut<=9999999):
    p1=segundoDigito*2
    p2=tercerDigito*3
    p3=cuartoDigito*4
    p4=quintoDigito*5
    p5=sextoDigito*6
    p6=septimoDigito*7
    p7=octavoDigito*2
    suma=p1+p2+p3+p4+p5+p6+p7
else:
    p1=primerDigito*2
    p2=segundoDigito*3
    p3=tercerDigito*4
    p4=cuartoDigito*5
    p5=quintoDigito*6
    p6=sextoDigito*7
    p7=septimoDigito*2
    p8=octavoDigito*3
    suma=p1+p2+p3+p4+p5+p6+p7+p8
restoDivision=suma%11
digito=11-restoDivision
dv=str(digito)
if (digito==11):
    dv="0"
if(digito==10):
    dv="K"
print("dv="+dv)