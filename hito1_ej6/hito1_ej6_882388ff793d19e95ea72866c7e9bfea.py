numero1=int(input("ingrese un numero"))
numero2=int(input("ingrese un numero"))
numero3=int(input("ingrese un numero"))
if(numero1<numero2 and numero1<numero3):
  menor=numero1
  if(numero2<=numero3):
    medio=numero2
    mayor=numero3
  else:
    medio=numero3
    mayor=numero2
if(numero2<=numero1 and numero2<numero3):
  menor=numero2
  if(numero1<=numero3):
    medio=numero1
    mayor=numero3
  else:
    medio=numero3
    mayor=numero1
else:
  menor=numero3
  if(numero1<=numero2):
    medio=numero1
    mayor=numero2
  else:
    medio=numero2
    mayor=numero1
print(menor,",",medio,",",mayor)