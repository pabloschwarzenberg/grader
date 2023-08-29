#Cálculo del dígito verificador de un rut
rut = str(input("ingrese su rut sin dv: "))

if len(rut)==8:
    n1=int(rut[7])*2
    n2=int(rut[6])*3
    n3=int(rut[5])*4
    n4=int(rut[4])*5
    n5=int(rut[3])*6
    n6=int(rut[2])*7
    n7=int(rut[1])*2
    n8=int(rut[0])*3
    sum=n1+n2+n3+n4+n5+n6+n7+n8
    r=11-(sum%11)
elif len(rut)==7:
    n1=int(rut[6])*2
    n2=int(rut[5])*3
    n3=int(rut[4])*4
    n4=int(rut[3])*5
    n5=int(rut[2])*6
    n6=int(rut[1])*7
    n7=int(rut[0])*2
    sum=n1+n2+n3+n4+n5+n6+n7
    r=11-(sum%11)
if r==11:
    r=0
elif r==10:
    r="K"
print("dv=",r)