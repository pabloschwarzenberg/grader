#Hito 1 descomponer numero
numero=input("Ingrese un numero de 4 digitos: ")
dig1=numero[0]
dig2=numero[1]
dig3=numero[2]
dig4=numero[3]
if int(dig1) > 0:
    print(dig1,"M +",dig2,"C +",dig3,"D +",dig4,"U")  
elif int(dig2) > 0:
    print(dig2,"C +",dig3,"D +",dig4,"U")
elif int(dig3) > 0:
    print(dig3,"D +",dig4,"U")
elif int(dig4) > 0:
    print(dig4,"U")
else:
    print("0 U")
