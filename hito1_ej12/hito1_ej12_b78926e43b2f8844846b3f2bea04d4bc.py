import random
n=random.randint(1,20)
k=5
while k>0:
  a=int(input("adivina mi número: "))
  if a==n:
      print ("Adivinaste, mi número era ",n)
      break
  if a>n:
        k=k-1
        if k==0:
            print("No adivinaste, mi número era ",n)
            break
        else:
            print("Prueba con un número más bajo")
  if a<n:
        k=k-1
        if k==0:
            print("No adivinaste, mi número era ",n)
            break
        else:
            print("¡Prueba con uno más alto!")

          

    
