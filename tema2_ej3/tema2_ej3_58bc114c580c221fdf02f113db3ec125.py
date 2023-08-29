def numero_perfecto(x):
   divisores = []
   for i in range(1, x):
       if x%i == 0:
           i = divisores.append(i)

   ##sumar divisores
   suma = 0
   for divisor in divisores:
       suma = suma + divisor
   if suma == x:
      esPerfecto = True
   else:
      esPerfecto = False
   return esPerfecto
if __name__=="__main__":
    u=int(input("Ingrese u: "))
    print(numero_perfecto(u))

           