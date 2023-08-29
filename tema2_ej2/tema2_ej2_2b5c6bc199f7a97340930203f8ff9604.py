# completa el código de la función
def amigos(x,y):

  d_1=1

  d_2=1

  s_1=0

  s_2=0

  while d_1<x:

    if x%d_1==0:

      s_1+=d_1

      

    d_1+=1

  while d_2<y:

    if y%d_2==0:

      s_2+=d_2

      

    d_2 += 1

  if s_1==y and s_2==x:

    return True

  else:

    return False

try:

 n_1 = int(input("Primer Número : "))

 n_2 = int(input("Segundo Número : "))

 print(amigos(n_1,n_2))

except:

 print("Porfavor ingrese un valor valido")
           