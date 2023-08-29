def convertidor(decimal):
  binario=''
  while (decimal//2)!=0:
    binario=str(decimal%2)+binario
    decimal=decimal//2
  return str(decimal) + binario
  
numero=int(input("Ingrese el numero a convertir: "))
print("resultado=",convertidor(numero))