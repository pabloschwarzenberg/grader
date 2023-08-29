#Descomponer un número
x = int(input("ingrese numero de 4 digitos: "))

a = x//1000
x = x%1000
b = x//100
x = x%100
c = x//10
x = x%10
d = x



if (a >= 1 and a <= 9 and b >= 0 and b <= 9
    and c >=0 and c <= 9 and d >= 0 and b <= 9):
    print(a,"m","+",b,"c","+", c,"d","+",d,"u")
    
elif (b >= 1 and b <= 9
    and c >=0 and c <= 9 and d >= 0 and b <= 9):
    print(b,"c","+", c,"d","+",d,"u")
    
elif (c >=1 and c <= 9 and d >= 0 and b <= 9):
    print(c,"d","+",d,"u") 

else:
    print(d,"u")




