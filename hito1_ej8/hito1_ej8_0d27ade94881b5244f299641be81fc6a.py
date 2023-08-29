print("ingrese un numero de hasta 4 digitos")
n = eval(input())
n1 = str(n)
n2 = len(n1)
if(n2 == 4):
    print(n1[0] + "M", "+", n1[1] + "C", "+", n1[2] + "D", "+", n1[3] + "U")
if(n2 == 3):
    print(n1[0] + "C", "+", n1[1] + "D", "+", n1[2] + "U")
if(n2 == 2):
    print(n1[0] + "D", "+", n1[1] + "U")
if(n2 == 1):
    print(n1[0] + "U")