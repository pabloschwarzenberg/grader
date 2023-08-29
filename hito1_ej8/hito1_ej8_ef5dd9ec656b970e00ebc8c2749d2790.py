#Descomponer un número
numero=int(input("ingrese numero de hasta 4 cifras:  "))

if 0 < numero < 9 :
    print(numero,"U")

elif  10< numero <99:
    a=numero%10
    b=numero//10
    print(b,"D ","+",a,"U")


elif 100<numero<999 :
    a=numero%10
    b=numero//10
    b%=10
    c=numero//10
    c=c//10
    print(c,"C ","+" ,b,"D ","+",a,"U")
    
elif 1000 < numero < 9999 :
    a=numero%10
    b=numero//10
    b%=10

    c=numero//100
    c%=10

    d=numero//1000

    print(d,"M ","+" , c,"C","+",b,"D ","+",a,"U")
