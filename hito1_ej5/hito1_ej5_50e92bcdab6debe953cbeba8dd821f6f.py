#Cálculo del dígito verificador de un rut
x=int(input("Ingrese numero:"))
a8=x//10000000
a7=x//1000000%10
a6=x%1000000//100000
a5=x%100000//10000
a4=x%10000//1000
a3=x%1000//100
a2=x%100//10
a1=x%10


b1=a1*2
b2=a2*3
b3=a3*4
b4=a4*5
b5=a5*6
b6=a6*7
b7=a7*2
b8=a8*3


y=b1+b2+b3+b4+b5+b6+b7+b8
pe=y//11
rde=y-(11*pe)
final=11-rde



if final== 11:
    print('dv=0')
elif final== 10:
    print('dv=K')
elif final!=11 and final!=10:
    print('dv=',final)      