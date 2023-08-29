a=int(input("Escriba un numero de 4 digitos:"))
b=a//1000
c=a-(1000*b)
d=c//100
e=c-(100*d)
f=e//10
h=e-(10*f)
print(str(b)+"M","+",str(d)+"C","+",str(f)+"D","+",str(h)+"U")

