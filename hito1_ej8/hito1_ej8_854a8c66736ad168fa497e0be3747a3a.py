    #Descomponer un número
num=int(input("Ingrese valor de 4 digitos a descomponer : "))
while not (num>=1 and num<=9999):
    num=int(input("ERROR... Ingrese un valor de 4 digitos :"))
if(num>=1000 and num<=9999):
    miles=num//1000
    num=num-(miles*1000)
    cientos=num//100
    num=num-(cientos*100)
    decenas=num//10
    num=num-(decenas*10)
    unidades=num//1
    num=num-(unidades*1)
    print(str(miles) + "M" "+" + str(cientos) + "C" "+" + str(decenas) + "D" "+" + str(unidades) + "U")
elif(num>=100 and num<=999):
    miles=num//1000
    num=num-(miles*1000)
    cientos=num//100
    num=num-(cientos*100)
    decenas=num//10
    num=num-(decenas*10)
    unidades=num//1
    num=num-(unidades*1)
    print(str(cientos) + "C" "+" + str(decenas) + "D" "+" + str(unidades) + "U")
elif(num>=10 and num<=99):
    miles=num//1000
    num=num-(miles*1000)
    cientos=num//100
    num=num-(cientos*100)
    decenas=num//10
    num=num-(decenas*10)
    unidades=num//1
    num=num-(unidades*1)
    print(str(decenas) + "D" "+" + str(unidades) + "U")
elif(num>=1 and num<=9):
    miles=num//1000
    num=num-(miles*1000)
    cientos=num//100
    num=num-(cientos*100)
    decenas=num//10
    num=num-(decenas*10)
    unidades=num//1
    num=num-(unidades*1)    
    print(str(unidades) + "U")