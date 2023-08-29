#Descomponer un número
numero=int(input("ingrese un numero:"))
n1=numero//1000
n2=numero//100%10
n3=numero//10%10
n4=numero%10
s1=str(n1)
s2=str(n2)
s3=str(n3)
s4=str(n4)
if  numero>=1000 and numero<=9999:
    print(s1+"M+",s2+"C+",s3+"D+",s4+"U")
elif    numero>=100 and numero<=999:
    print(s2+"C+",s3+"D+",s4+"U")
elif    numero>=10 and numero<=99:
    print(s3+"D+",s4+"U")
elif    numero>=0 and numero<=9:
    print(s4+"U")