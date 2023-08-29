#Descomponer un número
x = (input("ingrese un numero de maximo 4 digitos: "))
if len(x) == 4:
    print(x[0]+"M", "+", x[1]+"C", "+", x[2]+"D", "+", x[3]+"U")
elif len(x) == 3:
    print(x[0]+"C", "+", x[1]+"D", "+", x[2]+"U")
elif len(x) == 2:
    print(x[0]+"D", "+", x[1]+"U")
elif len(x) == 1:
    print(x[0]+"U")    
else:
    print("error")      