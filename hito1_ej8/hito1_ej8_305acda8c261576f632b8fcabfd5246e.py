n = input("Ingrese un numero de maximo 4 digitos: ")

if len(n) == 4:
    print(n[0],"M + ",n[1],"C + ",n[2],"D + ",n[3],"U")
elif len(n) == 3:
    print(n[0],"C + ",n[1],"D + ",n[2],"U")
elif len(n) == 2:
    print(n[0],"D + ",n[1],"U")
else:
    print("Ingrese un numero de maximo 4 digitos")