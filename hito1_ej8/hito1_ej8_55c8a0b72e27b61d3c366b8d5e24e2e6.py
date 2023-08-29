#entrada:ingrese un numero de maximo 4 digitos
#salida:mostrar la descomposicion
#el numero es:
n=int(input("el numero es: "))
while not(n>=0 and n<9999):
    n=int(input("el numero debe ser mayoy o igual a cero o menor a 9999: "))
#descomponer
largo=len(str(n))
if(largo==4):
    print(str(n)[0],"M+",str(n)[1],"C+",str(n)[2],"D+",str(n)[3],"U")
elif(largo==3):
    print(str(n)[0],"C+",str(n)[1],"D+",str(n)[2],"U")
elif(largo==2):
    print(str(n)[0],"D+",str(n)[1],"U")
elif(largo==1):
    print(str(n)[0],"U")
    