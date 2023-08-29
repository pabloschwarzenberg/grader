#Ecuaciones 

#Escritura de  la ecuacion

print("Forma Ax+By=C / Dx+Ey=F")

#Variables 
print("Agrege los numeros de la ecuacion de la A a la F")
A=int(input("A>"))
B=int(input("B>"))
C=int(input("C>"))
D=int(input("D>"))
E=int(input("E>"))
F=int(input("F>"))

print(A,"x +",B,"y =",C,"//",D,"x +",E,"y =",F)
#Resolucion
y=(F*A-D*C)/(E*A-B)
x=(C-B*y)/A
#solucion 
print("x=",x)
print("y=",y)