#Cálculo del dígito verificador de un rut
rut= int(input("Ingrese su rut, sin digito auntenticador: "))

n1=(rut//10000000)*3
n2=((rut//1000000)%10)*2
n3=((rut//100000)%10)*7
n4=((rut//10000)%10)*6
n5=((rut//1000)%10)*5
n6=((rut//100)%10)*4
n7=((rut//10)%10)*3
n8=((rut//1)%10)*2

suman=(n1+n2+n3+n4+n5+n6+n7+n8)
modulo11=suman//11
restodvsn=suman-(11*modulo11)
resultado=11-restodvsn

if resultado == 11:
    print("dv=",0)
elif resultado == 10:
    print("dv=", "k")
else:
    print("dv=",resultado)