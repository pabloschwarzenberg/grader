pokemon=33
nintendo=203
mario=28
ps4=348
fifa=51
bolsa1=0
bolsa2=0
bolsa3=0
bolsa4=0
bolsa5=0
contador=0
while (contador!=6):
    print(" juegos en venta")
    print("1. Pokemon X precio de 33.77" )
    print("2. Nintendo XL precio de 203")
    print("3. Mario Kart 7 precio de 27.58")
    print("4. PS4 precio de 348.000")
    print("5. FIFA precio de 51.19") 
    print("6. ver total")
    contador=contador+1
    if(contador==1):
      print("Pokemon agregado a la bolsa")
      bolsa1=bolsa1+pokemon
    elif(contador==2):
      print("Nintendo agregada a la bolsa")
      bolsa2=bolsa2+nintendo
    elif(contador==3):
      print("Mario agregado a la bolsa")
      bolsa3=bolsa3+mario
    elif(contador==4):
      print("Ps4 agregada a la bolsa")
      bolsa4=bolsa4+ps4
    elif(contador==5):
      print("Fifa agregado a la bolsa")
      bolsa5=bolsa5+fifa
    elif(contador==6):
      descuento1 = bolsa1+bolsa2+bolsa3
      total= bolsa1 + bolsa2 +  bolsa3 + bolsa4 + bolsa5 


descuento_max=((descuento1*20)/100)-descuento1

print(descuento1, "se le descuenta el 20% quedando", descuento_max)
print("su total es de",  total)