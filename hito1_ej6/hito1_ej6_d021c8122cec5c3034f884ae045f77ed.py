#Ordenar tres números
x1=int(input('ingrese un numero: '))
x2=int(input('ingrese un numero: '))
x3=int(input('ingrese un numero: '))

if x1<x2 and x2<x3:
    print(str(x1) +','+ str(x2) +','+ str(x3))
elif x1<x3 and x3<x2:
    print(str(x1) +','+ str(x3) +','+ str(x2))
elif x2<x1 and x1<x3:
    print(str(x2) +','+ str(x1) +','+ str(x3))
elif x2<x3 and x3<x1:
    print(str(x2) +','+ str(x3) +','+ str(x1))
elif x3<x1 and x1<x2:
    print(str(x3) +','+ str(x1) +','+ str(x2))
elif x1==x3 and x2<x3:
    print(str(x2) +','+ str(x1) +','+ str(x3))
elif x1==x3 and x2>x3:
    print(str(x1) +','+ str(x3) +','+ str(x2))    

else:
    print(str(x3) +','+ str(x2) +','+ str(x1))
