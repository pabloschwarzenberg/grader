#ENTRADA
Num =int(input("Ingrese el número del RUT: "))

#Cálculo dígito verificador

num1=((Num%10)*2)

num2=(((Num%100)//10)*3)

num3=(((Num%1000)//100)*4)

num4=(((Num%10000)//1000)*5)

num5=(((Num%100000)//10000)*6)

num6=(((Num//100000)%10)*7)

num7=(((Num//1000000)%10)*2)

num8=(((Num//10000000)*3))

#Cálculo
      
sumProds=num1 + num2 + num3 + num4 + num5 + num6+ num7 + num8

Mod = sumProds%11

DV = 11 - Mod

if DV == 11:
        print("dv=0")
elif DV == 10:
        print("dv=K")
else:
    print("dv= " +  str(DV))