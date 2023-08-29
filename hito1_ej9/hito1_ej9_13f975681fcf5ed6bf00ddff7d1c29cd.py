#Sistema de Ecuaciones
A=int(input("ingresar variable x1: "))
B=int(input("ingresar variable y1: "))
C=int(input("ingresar igualdad1: "))
D=int(input("ingresar variable x2: "))
E=int(input("ingresar variable y2: "))
F=int(input("ingresar igualdad2: "))
T=(((A*F)-(C*D)))
H=T/((A*E)-(B*D))
W=(((C-(B*H))/A))

X=round(W,1)
Y=round(H,1)

print("X=",X,"Y=",H)
      