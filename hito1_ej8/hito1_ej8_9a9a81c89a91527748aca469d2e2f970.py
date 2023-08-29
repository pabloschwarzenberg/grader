#Descomponer un número
numero =(input("Numero: "))


if int(numero) >= 10000:
    print("sus numeros ingresados estan icorrectos")

if int(numero) >= 1000 and int(numero) <= 9999:
    a = (numero[0])
    b = (numero[1])
    c = (numero[2])
    d = (numero[3])
    print(a,"M","+",b,"C","+",c,"D","+",d,"U")

if int(numero) >= 100 and int(numero) <= 999:
    a = (numero[0])
    b = (numero[1])
    c = (numero[2])
    print(a,"C","+", b,"D","+",c,"U")

if int(numero) >= 10 and int(numero) <= 99:
    a = (numero[0])
    b = (numero[1])
    print(a,"D","+",b,"U")

if int(numero) >= 1 and int(numero) <= 9:
    a = (numero[0])
    print(a,"U")

if numero == 0:
    print("no hay numero")