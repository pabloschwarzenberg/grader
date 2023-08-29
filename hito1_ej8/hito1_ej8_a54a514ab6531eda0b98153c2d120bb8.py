#Descomponer un número
a=str(input("Numero de 4 cifras: "))
if len(a) == 4:
    b = eval(a[0])
    c = eval(a[1])
    d = eval(a[2])
    e = eval(a[3])
    print(b,"M""+",c,"C""+",d,"D""+",e,"U")
elif len(a) == 3:
    b = eval(a[0])
    c = eval(a[1])
    d = eval(a[2])
    print(b,"C""+",c,"D""+",d,"U")
elif len(a) == 2:
    b = eval(a[0])
    c = eval(a[1])
    print(b,"D""+",c,"U")
elif len(a) == 1:
    b = eval(a[0])
    print(b,"U")