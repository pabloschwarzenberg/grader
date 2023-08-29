rut=int(input("Ingrese el rut: "))
digito1=rut % 10 #el octavo numero
resto=rut % 100
digito2=int(resto/10) #el septimo numero
resto2=rut % 1000
digito3=int(resto2/100) #el sexto numero
resto3=rut % 10000
digito4=int(resto3/1000) #el quinto numero
resto4=rut % 100000
digito5=int(resto4/10000) #el cuarto numero
resto5=rut % 1000000
digito6=int(resto5/100000) #el tercer numero
resto6=rut % 10000000
digito7=int(resto6/1000000) #el segundo numero
digito8=int(rut/10000000) #el primer numero

producto1=digito1 * 2
producto2=digito2 * 3
producto3=digito3 * 4
producto4=digito4 * 5
producto5=digito5 * 6
producto6=digito6 * 7
producto7=digito7 * 2
producto8=digito8 * 3

suma=(producto1+producto2+producto3+producto4+producto5+producto6+producto7+producto8)
division=int(suma/11)
resto0=suma-(11*division)
resta=11-resto0

if resta==11:
  print("dv=0")
if resta==10:
  print("dv=K")
if resta<=9 and resta>=0:
  print("dv=", resta)