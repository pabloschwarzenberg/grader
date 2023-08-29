#a
variante=0
n=int(input("Ingrese un numero(MAX 4 DIGITOS)"))
while n > 9999:
    n=int(input("Ingrese un numero"))

if n <10000:
        if n > 999:
            variante = 1
        elif n > 99:
            variante = 2
        elif  n > 9:
            variante = 3
        elif  n < 10 :
            variante = 4

if variante == 1:
    m=int(str(n)[0])
    c=int(str(n)[1])
    d=int(str(n)[2])
    u=int(str(n)[3])

    print(m,"M ","+", c,"C","+", d,"D","+", u,"U")
elif variante== 2:
    c=int(str(n)[0])
    d=int(str(n)[1])
    u=int(str(n)[2])
    print(c,"C","+",d,"D","+",u,"U")
elif variante ==3:
    d=int(str(n)[0])
    u=int(str(n)[1])
    print(d,"D","+",u,"U")
elif variante == 4 :
    u=int(str(n)[1])
    print(u,"U")
