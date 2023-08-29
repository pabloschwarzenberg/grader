#Descomponer un número
num = str(input("ingrese un numero de maximo 4 digitos a descomponer: "))
if(len(num) == 4):
    n1 = num[0]
    n2 = num[1]
    n3 = num[2]
    n4 = num[3]
    print(n1,"M +" ,n2,"C +" ,n3,"D +", n4,"U")
elif(len(num) == 3):
    n1 = num[0]
    n2 = num[1]
    n3 = num[2]
    print(n1,"C +", n2,"D +", n3,"U ")
elif (len (num) == 2):
    n1 = num[0]
    n2 = num[1]
    print(n1,"D +", n2,"U ")
elif (len (num) == 1):
    n1 = num[0]
    print(n1,"U")