#Descomponer un número
x=str(input("Numero de 4 cifras: "))
if len(x) == 4:
    b = eval(x[0])
    c = eval(x[1])
    d = eval(x[2])
    e = eval(x[3])
    print(b,"M""+",c,"C""+",d,"D""+",e,"U")
elif len(x) == 3:
    b = eval(x[0])
    c = eval(x[1])
    d = eval(x[2])
    print(b,"C""+",c,"D""+",d,"U")
elif len(x) == 2:
    b = eval(x[0])
    c = eval(x[1])
    print(b,"D""+",c,"U")
elif len(x) == 1:
    b = eval(x[0])
    print(b,"U")