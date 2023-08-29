#Descomponer un número
numero=eval(input("ingresar un Numero de hasta 4 digitos:"))
while not(numero>0 and numero<9999):
    numero=eval(inpt("Error favor ingrese un numero de 4 digitos:"))
largo=len(str(numero))
if largo==4:
    unidad=str(numero)[-1]
    decena=str(numero)[2]
    centena=str(numero)[1]
    mil=str(numero)[0]
    print("Numero descompuesto es:",mil,"M + ",centena, "C + ",decena, "D + ",unidad, "U")
if largo==3:
    unidad=str(numero)[-1]
    decena=str(numero)[1]
    centena=str(numero)[0]
    print("Numero descompuesto es:", centena, "C + ", decena, "D + ", unidad, "U")
if largo==2:
    unidad=str(numero)[-1]
    decena=str(numero)[0]
    print("Numero descompuesto es:", decena, "D + ", unidad, "U")
if largo==1:
    unidad=str(numero)[0]
    print("Numero descompuesto es:", unidad, "U")