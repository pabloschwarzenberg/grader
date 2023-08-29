#Sistema de Ecuaciones
a=float (input("ingrese variable de a^2"))
b=float(input("ingrese variable de b"))
c=float(input("ingrese variable de c"))
ps1=b**2-4*a*c
ps2=ps1**0.5
ps3=-b-ps2
ps32=-b+ps2
ps42=ps32/2*a
ps4=ps3/2*a
z=(ps4)
x=(ps42)
print("primera solucion",z)
print("segunda solucion",x)      