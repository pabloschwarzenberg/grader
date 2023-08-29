#Contestador de celular
#valor=45321567%1000
#print(f"{valor}")
#definiciendo y iniciaizando
fono=int(input("Ingrese el número telefónico de 8 dígitos: "))
anexoTermina=fono%1000   #asignnado
anexoComienza= fono//100000
hora=input("Ingrese la hora en formato hh ") #trabajar con dos caracteres
if hora >='00' and hora <='07':
  print("CONTESTAR")
elif hora<'14' and anexoTermina == 909:
  print("CONTESTAR")
elif hora >='17' and hora <='19' and anexoComienza != 877:
  print("CONTESTAR")
elif hora>'19':
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")