# Sistema de Ecuaciones
# 2X+3Y=6
# X+2Y=5
# 1st
print("Primera ecuación:")
pos1=float(input("1. Ingrese su dígito X:"))
pos2=float(input("2. Ingrese su dígito Y:"))
pos3=float(input("3. Ingrese su resultado:"))
# 2nd
print("Segunda ecuación:")
pos4=float(input("1. Ingrese su dígito X:"))
pos5=float(input("2. Ingrese su dígito Y:"))
pos6=float(input("3. Ingrese su resultado:"))
# 2do metodo (incompleto)w
#for a in pos1,pos4:
#    str(a)+"X"
#for b in pos2,pos5:
#    str(b)+"Y"

# proceso del sistema
res=(pos1*pos5)-(pos2*pos4)
# EJ: 2X + 3Y = 6
if(res!=0):
    x=((pos3*pos5)-(pos2*pos6)) / res
    y=((pos1*pos6)-(pos3*pos4)) / res
    if(x==float(-0)):
        print("x=",abs(x.__round__(1)))
    else:
        print("x=",x.__round__(1))
    print("y=",y.__round__(1))
    #nose cual es la diferencia entre estos 2 pero creo que ambos sirven?
    #print("x=",round(x,1))
    #print("y=",round(y,1))