#Descomponer un número
numero = int(input("Ingrese un numero entero (de 4 digitos) ")) #4

if len(str(numero)) == 1:
   print(numero)
elif len(str(numero)) == 2:
   print("%sD + %sU" %(str(numero)[0],str(numero)[1]))
elif len(str(numero)) == 3:
   print("%sC + %sD + %sU" %(str(numero)[0],str(numero)[1],str(numero)[2]))
elif len(str(numero)) == 4:
   print("%sM + %sC + %sD + %sU" %(str(numero)[0],str(numero)[1],str(numero)[2],str(numero)[3]))
else:
   print("Solo digitos de hasta 4 digitos")
      