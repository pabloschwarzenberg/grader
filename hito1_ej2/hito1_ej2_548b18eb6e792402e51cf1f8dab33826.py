t= eval(input("ingrese numero telefonico:"))
h= eval(input("ingrese hora de llamada:"))
ni = t // 100000
nf = t % 1000

if h >= 0 and h <= 7:
    print ("Resultado: CONTESTAR")
if h <= 14:
  if nf == 909:
    print("resultado: CONTESTAR")
if h >= 17 and h <= 19:
   if ni == 877:
    print ("resultado: NO CONTESTAR")
if h > 19:
    print("Resultado: NO CONTESTAR")