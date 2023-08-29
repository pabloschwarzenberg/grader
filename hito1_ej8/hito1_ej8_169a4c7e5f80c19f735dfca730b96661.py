#Descomponer un número
num = float(input("ingrese numero: "))
um = num/1000
pan = num % 1000

c = pan/100
pan = pan % 100

d = pan/10
u = pan%10

print("M: %i" %um)
print("C: %i" %c)
print("D: %i" %d)
print("U: %i" %u)

if um <= 0:
  print(c,"C+",d,"D+",u,"U")
  if c<=0:
    print(d,"D+",u,"U")
    if d<=0:
      print(u,"U")
if um>0:
  print("%i"%um,"M+","%i"%c,"C+","%i"%d,"D+","%i"%u,"U")