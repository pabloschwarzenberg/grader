#Aprobación de créditos                                                                                                                  
Ingreso=int(input("ingrese el monto de credito en pesos:"))
Nacimiento=int(input("ingrese su año de nacimiento:"))
Hijos=int(input("ingrese su numero de hijos:"))
Antiguedad=int(input("ingrese los años de antiguedad en el banco:"))
Estadocivil=str(input("Ingrese su estado civil (Casado=C,Soltero=S):"))
Residencia=str(input("Ingrese si su residencia es Rural(R) o Urbana(U):"))
#El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if(Antiguedad>10 and Hijos>=2):
  print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif(Estadocivil=="C" and Hijos>3 and 1962<=Nacimiento<=1972):
  print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif(Ingreso>2500000 and Estadocivil=="S" and Residencia=="U"):
  print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif(Ingreso>3500000 and Antiguedad>5):
  print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif(Residencia=="R" and Estadocivil=="C" and Hijos<2):
  print("APROBADO")
