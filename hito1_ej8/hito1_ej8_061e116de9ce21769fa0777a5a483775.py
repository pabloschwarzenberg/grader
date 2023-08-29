#Descomponer un número
num=int(input("ingrese numero "))
mil=(num//1000)
cen=(num-(mil*1000))//100
res1=(num//100)
res2=(num-(res1*100))
dec=(res2//10)
uni=(res2-(dec*10))
if(num<=999):
    print(cen,"C+",dec,"D+",uni,"U")
elif(num<=9999):
    print(mil,"M+",cen,"C+",dec,"D+",uni,"U")
else:
    print("ingreso un numero con mas de 4 digitos")