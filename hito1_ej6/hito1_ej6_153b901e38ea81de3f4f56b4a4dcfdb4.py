#Ordenar tres números
a=input("Ingrese un numero entero: ")
b=input("Ingrese un numero entero: ")
c=input("Ingrese un numero entero: ")
d=max(a,b,c)
e=min(a,b,c)
if a==d and b==e:
    medio=c
    print(str(e)+", "+str(medio)+", "+str(d))
if b==d and a==e:
    medio=c
    print(str(e)+", "+str(medio)+", "+str(d))
if c==d and b==e:
    medio=a
    print(str(e)+", "+str(medio)+", "+str(d))
if b==d and c==e:
    medio=a
    print(str(e)+", "+str(medio)+", "+str(d))
if c==d and a==e:
    medio=b
    print(str(e)+", "+str(medio)+", "+str(d))
if a==d and c==e:
    medio=b
    print(str(e)+", "+str(medio)+", "+str(d)) 

    
     