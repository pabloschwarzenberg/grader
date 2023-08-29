#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))

primer_digito_rut =(rut//10000000) * 3

segundo_digito_rut =((rut//1000000)%10) * 2

tercer_digito_rut =((rut//100000)%10) * 7

cuarto_digito_rut =((rut//10000)%10) * 6

quinto_digito_rut =((rut//1000)%10) * 5

sexto_digito_rut =((rut//100)%10) * 4

septimo_digito_rut =((rut//10)%10) * 3

octavo_digito_rut =((rut//1)%10) * 2

suma = sum([primer_digito_rut, segundo_digito_rut, tercer_digito_rut, cuarto_digito_rut, quinto_digito_rut, sexto_digito_rut, septimo_digito_rut, octavo_digito_rut])

resto1 = suma // 11

resto2 = suma-(11*resto1)

resta_de_digitos = 11-resto2

if resta_de_digitos == 11:

  print("dv=",end="")

  print(0)

elif resta_de_digitos == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end="")
  print(resta_de_digitos)      