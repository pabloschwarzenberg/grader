#Cálculo del dígito verificador de un rut
Rut = int(input("Ingrese el rut sin digito verificador: "))

Primerdig = (Rut//10000000) * 3
Segundodig = ((Rut//1000000)%10) * 2
Tercerdig = ((Rut//100000)%10) * 7
Cuartodig = ((Rut//10000)%10) * 6
Quintodig = ((Rut//1000)%10) * 5
Sextodig = ((Rut//100)%10) * 4
Septimodig = ((Rut//10)%10) * 3
Octavodig = ((Rut//1)%10) * 2

suma = (Primerdig + Segundodig + Tercerdig + Cuartodig + Quintodig + Sextodig + Septimodig + Octavodig)

resto1 = suma // 11
resto2 = suma - (11 * resto1)
resta = 11 - resto2
if resta == 11:
  print("dv= ",end="")
  print(0)
elif resta == 10:
  print("dv= ",end="")
  print("k")
else:
  print("dv= ",end="")
  print(resta)      