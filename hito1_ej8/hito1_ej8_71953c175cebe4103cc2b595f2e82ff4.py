#Descomponer un número
numero=eval(input("Ingrese un numero de 4 digitos:"))
while not (numero>0 and numero<9999):
    numero=eval(input("ERROOOOR Ingrese un numero de 4 digitos:"))
largo=len(str(numero))
if largo==4:
    unidad= str(numero)[-1]
    mil=str(numero)[0]
    centena= str(numero)[1]
    decena=str(numero)[2]
    print("El numero descompuesto es: ",mil,"M + ",centena,"C + ",decena,"D + ",unidad,"U")
if largo==3:
    unidad=str(numero)[-1]
    centena=str(numero)[0]
    decena=str(numero)[1]
    print("El numero descompuesto es ",centena,"C + ",decena,"D + ",unidad,"U")   
if largo==2:
    decena=str(numero)[0]
    unidad=str(numero)[-1]
    print("El numero descompuesto es ",decena,"D + ",unidad,"U")  
if largo==1:
    unidad=str(numero)[0]
    print("El numero descompuesto es ",unidad,"U")     