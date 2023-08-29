# completa el código de la función
a = int(input("número a: "))
b = int(input("número b: "))

atotal = 1
i = 2
while (i<a):
      r = a%i
      if (r==0):
          atotal = atotal+i
      i = i+1

btotal = 1
j = 2
while (j<b):
      r = b%j
      if (r==0):
          btotal = btotal+j
      j = j+1

if (atotal==b and btotal==a):
      namigos = 1
else:
      namigos = 0

print(namigos)