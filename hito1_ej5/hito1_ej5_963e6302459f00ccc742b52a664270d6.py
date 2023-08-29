#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut sin puntos ni guión y sin dígito verificador:"))
rut2=(rut//1)%10
rut3=(rut//10)%10
rut4=(rut//100)%10
rut5=(rut//1000)%10
rut6=(rut//10000)%10
rut7=(rut//100000)%10
rut8=(rut//1000000)%10
rut9=(rut//10000000)%10
mult1=rut2*2
#print("Mult1",mult1)
mult2=rut3*3
#print("Mult2",mult2)
mult3=rut4*4
#print("Mult3",mult3)
mult4=rut5*5
#print("Mult4",mult4)
mult5=rut6*6
#print("Mult5",mult5)
mult6=rut7*7
#print("Mult6",mult6)
mult7=rut8*2
#print("Mult7",mult7)
mult8=rut9*3
#print("Mult8",mult8)
sumaProductos=mult1+mult2+mult3+mult4+mult5+mult6+mult7+mult8
#print("sumaProductos",sumaProductos)
divSumaProductos=sumaProductos//11
x=sumaProductos-(11*divSumaProductos)
digito=11-x
digitoVerificador=0
#print(digito)
if digito==11:
    digitoVerificador=0
elif digito==10:
    digitoVerificador="k"
else:
    digitoVerificador=digito
print("dv=",digitoVerificador)