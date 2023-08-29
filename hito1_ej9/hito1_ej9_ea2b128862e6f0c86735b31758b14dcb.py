x1=float(input("Valor de X: "))
y1=float(input("Valor de Y:"))
n1=float(input("Valor numerico: "))
x2=float(input("Valor de X: "))
y2=float(input("Valor de Y:"))
n2=float(input("Valor numerico: "))

valor_de_x=(-y1*x2+y2*x1)
valor_numero=(-y1*n2+y2*n1)

if(valor_de_x<0) and(valor_numero<0) or(valor_de_x<0) and(valor_numero>0):
    paso1=float(valor_de_x)
    paso2=float(valor_numero)
    paso3=(paso1*-1)
    paso4=(paso2*-1)
    paso5=(paso4/paso3)
    paso6=float(paso5)
    paso7=("%.1f"%paso6)
    print("x=",paso7)

elif(valor_de_x==-1) and(valor_numero<0) or(valor_numero>0):
    paso1=float(valor_numero)
    paso2=(paso1*-1)
    paso3=("%.1f"%paso2)
    print("x=",paso3)

elif(valor_de_x==1) and(valor_numero<0) or(valor_numero>0):
    paso1=float(valor_numero)
    paso2=("%.1f"%paso1)
    print("x=",paso2)

elif(valor_de_x>0) and(valor_numero>0) or(valor_de_x>0) and(valor_numero<0):
    paso1=float(valor_de_x)
    paso2=(paso1*-1)
    paso3=(valor_numero/paso2)
    paso4=float(paso3)
    paso5=("%.1f"%paso4)
    print("x=",paso5)

elif(valor_de_x>0) and(valor_numero==0) or(valor_de_x<0) and(valor_numero==0):
    paso1=float(valor_de_x)
    paso2=(paso1*-1)
    paso3=("%.1f"%paso2)
    print("x=",paso3)
else:
    print("Ingrese otros numeros")
#--------OPERATORIA EN Y------------
valor_de_y=(-x1*y2+x2*y1)
valor_numero2=(-x1*n2+x2*n1)

if(valor_de_y<0) and(valor_numero2<0) or(valor_de_y<0) and(valor_numero2>0):
    paso1=float(valor_de_y)
    paso2=float(valor_numero2)
    paso3=(paso1*-1)
    paso4=(paso2*-1)
    paso5=(paso4/paso3)
    paso6=float(paso5)
    paso7=("%.1f"%paso6)
    print("y=",paso7)

elif(valor_de_y==-1) and(valor_numero2<0) or(valor_numero2>0):
    paso1=float(valor_numero2)
    paso2=(paso1*-1)
    paso3=("%.1f"%paso2)
    print("y=",paso3)

elif(valor_de_y==1) and(valor_numero2<0) or(valor_numero2>0):
    paso1=float(valor_numero22)
    paso2=("%.1f"%paso1)
    print("y=",paso2)

elif(valor_de_y>0) and(valor_numero2>0) or(valor_de_y>0) and(valor_numero2<0):
    paso1=float(valor_de_y)
    paso2=(paso1*-1)
    paso3=(valor_numero/paso2)
    paso4=float(paso3)
    paso5=("%.1f"%paso4)
    print("y=",paso5)

elif(valor_de_y>0) and(valor_numero2==0) or(valor_de_y<0) and(valor_numero2==0):
    paso1=float(valor_de_y)
    paso2=(paso1*-1)
    paso3=("%.1f"%paso2)
    print("y=",paso3)
else:
    print("Ingrese otros numeros")