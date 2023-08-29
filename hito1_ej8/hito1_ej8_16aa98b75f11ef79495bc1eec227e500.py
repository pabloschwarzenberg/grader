#Descomponer un número.1230
num = input("Número hasta de cuatro digitos : ")
Cnum = len(num)

if Cnum == 1:
     print(num +"U")

if Cnum == 2:
    u = num[1:2]
    d = num[0:1]
    print(d +"D","+",u +"U")

if Cnum == 3:
    u = num[2:3]
    d =num[1:2]
    c = num[0:1]
    print(c +"C","+",d +"D","+",u +"U")

if Cnum == 4:
    u = num[3:4]
    d = num[2:3]
    c = num[1:2]
    um = num[0:1]
    print(um + "M","+",c +"C","+",d +"D","+",u +"U")
