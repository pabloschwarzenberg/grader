#Descomponer un número
n=input("ingrese un n nunmero de 4 digiitos :")

if len(n)==1:
    print(n+"U")
elif len(n)==2 :
    print(n[0]+"D","+",n[-1]+"U")
elif len(n)==3:
    print(n[0]+"C","+",n[-2]+"D","+",n[-1]+"U")
else :
    print(n[0]+"M","+",n[-3]+"C","+",n[-2]+"D","+",n[-1]+"U")