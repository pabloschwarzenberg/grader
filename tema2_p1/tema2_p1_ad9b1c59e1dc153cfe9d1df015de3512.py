def es_primo(num):
   if num<2:
      return False
   for i in range(2,num):
      if num%i==0:
         return False
   return True
n=int(input("ingrese numero: "))
print(es_primo(n))
