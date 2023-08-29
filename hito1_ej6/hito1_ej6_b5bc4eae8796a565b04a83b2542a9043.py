N1=int(input("Ingrese el primer numero: "))
N2=int(input("Ingrese el segundo numero: "))
N3=int(input("Ingrese el tercer numero: "))
if N1>=N2>=N3:
  print(f"{N1},{N2},{N3}")
elif N1>=N3>=N2:
  print(f"{N1},{N3},{N2}")
elif N2>=N1>=N3:
  print(f"{N2},{N1},{N3}")
elif N2>=N3>=N1:
  print(f"{N2},{N3},{N1}")
elif N3>=N1>=N2:
  print(f"{N3},{N1},{N2}")
elif N3>=N2>=N1:
  print(f"{N3},{N2},{N1}")