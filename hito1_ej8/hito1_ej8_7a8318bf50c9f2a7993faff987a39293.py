#Descomponer un número
num=[int(x) for x in input("Ingrese un número de hasta 4 dígitos: ")]
n=len(num)
lista=num
if n == 4:
    a=lista[n-4]
    b=lista[n-3]
    c=lista[n-2]
    d=lista[n-1]
    print(a,"M +", b ,"C +", c ,"D +", d, "U")
elif n == 3:
    q=lista[n-3]
    w=lista[n-2]
    e=lista[n-1]
    print(q ,"C +", w ,"D +", e, "U")
elif n == 2:
    z=lista[n-2]
    x=lista[n-1]
    print(z ,"D +", x, "U")
elif n == 1:
    j=lista[n-1]
    print(j , "U")
else:
    print("Número invalido")
      