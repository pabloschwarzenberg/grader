#Ordenar tres números
print("Escriba tres numeros enteros al lado de las letras a, b, c:")
a=int(input("Numero a: "))
b=int(input("Numero b: "))
c=int(input("Numero c: "))
if a/b<=1:
    if b/c<=1:
        a=str(a)
        b=str(b)
        c=str(c)
        print(""+a+","+b+","+c+"")
    else:
        a=str(a)
        b=str(b)
        c=str(c)
        print(""+a+","+c+","+b+"")
else:
    if a/c<=1:
        a=str(a)
        b=str(b)
        c=str(c)
        print(""+b+","+a+","+c+"")
    else:
        a=str(a)
        b=str(b)
        c=str(c)
        print(""+b+","+c+","+a+"")

