#Sistema de Ecuaciones

print("resolvamos un sistema de ecuacios de dos incognitas\nde la forma\nax+by=c\ndx+ey=f")
ax=int(input("ingrese el valor de a: "))
by=int(input("ingrese el valor de b: "))
cc=int(input("ingrese el valor de c: "))
dx=int(input("ingrese el valor de d: "))
ey=int(input("ingrese el valor de e: "))
ff=int(input("ingrese el valor de f: "))

#para x

nby=by*-dx
ney=ey*ax
ncc=cc*-dx
nff=ff*ax


nn=nby+ney
nn1=ncc+nff
solvey=(nn1)/(nn)

#para y
nax=ax*-ey
ndx=dx*by
nncc=cc*-ey
nnff=ff*by


nnn=nax+ndx
nnn1=nncc+nnff
solvex=(nnn1)/(nnn)

print("x=",round(solvex, 1), "y=",round(solvey,1))