

numero=int(input("escribe un numero hasta 4 numeros:    "))
num=str(numero)

if numero <=9999 and numero >999 :
    m=num[-4]
    c=num[-3]
    d=num[-2]
    u=num[-1]
    print("" , m,"M +",c,"C +",d,"D +", u ,"U" )
elif numero <=999 and numero >99:
    c=num[-3]
    d=num[-2]
    u=num[-1]
    print("",c,"C +",d,"D +", u ,"U" )
elif numero <=99 and numero >9:
    d=num[-2]
    u=num[-1]
    print("",d,"D +", u ,"U" )
elif numero <=9 :
    u=num[-1]
    print("", u,"U")      