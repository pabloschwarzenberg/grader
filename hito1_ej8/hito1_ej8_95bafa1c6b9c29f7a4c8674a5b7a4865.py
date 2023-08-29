#Descomponer un número
n = eval(input("Ingrese un número de hasta 4 digitos: "))

if n/1000 >=1:
    w = str(n)
    print(w[0],"M","+",w[1],"C","+",w[2],"D","+",w[3],"U")
elif n/100 >=1:
    w = str(n)
    print(w[0],"C","+",w[1],"D","+",w[2],"U")
elif n/10 >=1:
    w = str(n)
    print(w[0],"D","+",w[1],"U")
elif n/1 >=1:
    w = str(n)
    print(w[0],"U")     