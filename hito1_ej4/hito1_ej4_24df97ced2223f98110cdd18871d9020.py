numero=int(input("introducir decimal"))
nuevo=numero
binario = ''
while (nuevo!=0):
  binario+=str(nuevo % 2)
  nuevo = nuevo//2

print ("resultado=",binario[::-1])
  