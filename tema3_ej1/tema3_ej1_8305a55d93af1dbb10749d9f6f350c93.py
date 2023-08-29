def suma_divisores(a):
  suma=0
  for numero in range(1,a+1):
        if a % numero == 0 :
          suma = suma + numero
  if (suma-a)!=1:
      return (suma-a,False)
  if (suma-a)==1:
      return (suma-a,True)

      
 
           