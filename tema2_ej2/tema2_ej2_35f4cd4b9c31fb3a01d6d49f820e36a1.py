# completa el código de la función
def amigos(a,b):
  dn=1
  dn_2=1
  sn=0
  sn_2=0
  while dn<a:
    if a%dn==0:
      sn+=dn
    dn+=1
  while dn_2<b:
    if b%dn_2==0:
      sn_2+=dn_2
    dn_2 += 1
  if sn==b and sn_2==a:
    return True
  else:
    return False
try:
 num = int(input("Número 1: "))
 num_2 = int(input("Número 2: "))
 print(amigos(num,num_2))
except:
 print("Por favor Ingrese un Número") 