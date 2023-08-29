#Cálculo del dígito verificador de un rut
r= int(input("ingrese rut : "))

a=(r%10)*2
b= (int((r%100)/10))*3
c= (int(r%1000/100))*4
d= (int(r%10000/1000))*5
e= (int(r%100000/10000))*6
f= (int(r%1000000/100000))*7
g= ((r//1000000)%10)*2
h=  (r//10000000)*3

resto = (a+b+c+d+e+f+g+h)%11
digito = 11-resto

if digito== 11:
    print("dv=0")
elif digito== 10:
    print("dv=k")
else :
    print("dv=",end="") 
    print(digito)
    