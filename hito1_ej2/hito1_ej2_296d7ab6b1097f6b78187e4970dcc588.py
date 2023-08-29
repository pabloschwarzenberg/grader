fono=int(input("Ingrese el número telefónico de 8 dígitos: "))
Termina=fono%1000
Comienza= fono//100000
hora=input("Ingrese la hora en formato 24 hrs ") 
if hora >='00' and hora <='07':
  print("CONTESTAR")
elif hora<'14' and Termina == 909:
  print("CONTESTAR")
elif hora >='17' and hora <='19' and Comienza != 877:
  print("CONTESTAR")
elif hora>'19':
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")     