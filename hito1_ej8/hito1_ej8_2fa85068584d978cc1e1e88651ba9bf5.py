#Descomponer un número
x = eval(input("Ingrese un número de hasta 4 digitos: "))

if x/1000 >=1:
    w = str(x)
    print(w[0],"M","+",w[1],"C","+",w[2],"D","+",w[3],"U")
elif x/100 >=1:
    w = str(x)
    print(w[0],"C","+",w[1],"D","+",w[2],"U")
elif x/10 >=1:
    w = str(x)
    print(w[0],"D","+",w[1],"U")
elif x/1 >=1:
    w = str(x)
    print(w[0],"U")     