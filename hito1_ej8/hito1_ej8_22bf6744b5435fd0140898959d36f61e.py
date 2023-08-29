p=int(input("Ingrese un numero de maximo 4 cifras: "))

w=p//1000

x=(p//100)-(w*10)

y=(p//10)-((x*10)+(w*100))

z=(p)-((y*10)+(x*100)+(w*1000))

a="M +"
b="C +"
c="D +"
d="U"

if w==0 and x==0 and y==0:
    print("La descomposicion del numero es: ",z,d)

elif w==0 and x==0:
    print("La descomposicion del numero es: ",y,c,z,d)

elif w==0:
    print("La descomposicion del numero es: ",x,b,y,c,z,d)

else:
    print("La descomposicion del numero es: ",w,a,x,b,y,c,z,d)