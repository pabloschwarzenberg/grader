#Ordenar tres números
a=input()
b=input()
c=input()
if(a>=b>=c):
    mayor=a
    medio=b
    menor=c
if(a>=c>=b):
    mayor=a
    medio=c
    menor=b
if(b>=a>=c):
    mayor=b
    medio=a
    menor=c
if(b>=c>=a):
    mayor=b
    medio=c
    menor=a
if(c>=a>=b):
    mayor=c
    medio=a
    menor=b
        
if(c>=b>=a):
    mayor=c
    medio=b
    menor=a
       
        
print(menor+",",medio+",",mayor)
