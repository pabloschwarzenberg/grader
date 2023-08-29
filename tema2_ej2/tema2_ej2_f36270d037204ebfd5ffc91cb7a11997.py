# completa el código de la función
def amigos(a,b):
  return
 

def sumaDe(num):

   x = 0

   for i in range(1, num):

       if num % i == 0 and i != num:

           print(i)

           x += i

   return x

z = int(input("Número dado "))

nums = []

for i in range(1, z):

   for j in range(1, z):

       if i == sumaDe(j) and j == sumaDe(i) and i != j:

           nums.append(i)

print(nums)
           