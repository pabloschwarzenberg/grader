#Descomponer un número
numero=int(input("Ingrese numero:"))

if len(str(numero))==1:
    print(str(numero)+"U")

elif len(str(numero))==2:
    n1=numero//10
    n2=numero%10
    print(str(n1)+"D"+"+"+str(n2)+"U")

elif len(str(numero))==3:
    n1= numero//100
    n2= numero//10%10
    n3= numero%10 
    print(str(n1)+"C"+"+"+str(n2)+"D"+"+"+str(n3)+"U")
elif len(str(numero))==4:
    n1= numero//1000
    n2=numero//100%10
    n3= numero//10%10
    n4= numero%10
    print(str(n1)+"M"+"+"+str(n2)+"C"+"+"+str(n3)+"D"+"+"+str(n4)+"U")
