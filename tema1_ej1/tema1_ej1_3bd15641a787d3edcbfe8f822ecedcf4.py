#Suma de los N primeros números
def sumadigitos(num):
    s=0
    while num>0:
        s=s+num%10
        num=num//10
    return s

n= int(input("cantidad de numero: "))
sumay= 0
if__name__ =="__main__":
  while n> 0:
    num=int(input("numero: "))
    sumay=sumay+sumadigitos(num)
    n=n-1
print(sumay)     