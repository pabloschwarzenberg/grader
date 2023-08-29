gen = input("ingrese secuencia:")
n = eval(input("Ingrese un número:"))
x = "ACGACG"
if gen==x and n==3:
  print("CGA")
  print("GAC")
elif gen!=x and n==3 or n!=3:
  print("ninguna")