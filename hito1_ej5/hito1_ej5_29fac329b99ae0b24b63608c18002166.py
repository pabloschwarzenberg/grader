#Cálculo del dígito verificador de un rut
rut=int(input())

a=(rut%10)*2
b=((rut%100)//10)*3
c=((rut%1000)//100)*4
d=((rut%10000)//1000)*5
e=((rut%100000)//10000)*6
f=((rut%1000000)//100000)*7
g=((rut%10000000)//1000000)*2
h=((rut%100000000)//10000000)*3

suma=a+b+c+d+e+f+g+h

resto=suma%11

digito=11-resto

if(digito==10):
    print("dv=k")
elif(digito==11):
    print("dv=0")
else:
    print("dv="+str(digito))
    