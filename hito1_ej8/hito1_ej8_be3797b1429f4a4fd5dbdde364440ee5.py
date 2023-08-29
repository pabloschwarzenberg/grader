#Descomponer un número
numero=int(input("ingrese el numero: "))

a=numero//1000
b=(numero-(a*1000))//100
c=(numero-(a*1000 + b*100))//10
d=(numero-(a*1000 + b*100 + c*10 ))//1


if len(str(numero))==4:
    print(a,"M","+",b,"C","+",c,"D","+",d,"U")

elif len(str(numero))==3:
    print(b,"C","+",c,"D","+",d,"U")
    
elif len(str(numero))==2:
    print(c,"D","+",d,"U")

else:
    print(d,"U")         