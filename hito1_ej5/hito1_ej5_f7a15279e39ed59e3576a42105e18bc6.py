numero = int(input("Ingrese rut:"))
rut = str(numero)

contador = 0
nume = 3
if len(rut) == 7:
    nume = 2
for num in range (0,len(rut)):
      var = int(rut[num])*nume
      contador += var
      nume -= 1
      if nume == 1:
        nume = 7

division = contador % 11
digito = 11 - division
if digito == 11:
    digito =0
elif digito == 10 :
    digito = "k"
digitoconvertido = str(digito)

print("dv=" + digitoconvertido)

