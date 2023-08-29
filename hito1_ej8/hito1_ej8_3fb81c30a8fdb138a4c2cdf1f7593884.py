#Descomponer un número
     n=int(input("Ingrese un numero de 4 digitos: "))
while not (n>0 and n<9999):
    numero=int(input("no haz inscrito un valor de 4 digitos: "))
largo=len(str(n))
if (largo==4):
    unidad= str(n)[-1]
    mil=str(n)[0]
    centena= str(n)[1]
    decena=str(n)[2]
    print("se descompone en ",mil,"M + ",centena,"C + ",decena,"D + ",unidad,"U")
elif(largo==3):
    unidad=str(n)[-1]
    centena=str(n)[0]
    decena=str(n)[1]
    print("se descompone en ",centena,"C + ",decena,"D + ",unidad,"U")   
elif(largo==2):
    decena=str(n)[0]
    unidad=str(n)[-1]
    print("se descompone en ",decena,"D + ",unidad,"U")  
elif(largo==1):
    unidad=str(n)[0]
    print("se descompone en ",unidad,"U")
else:
    print("no se coloco un valor numerico")