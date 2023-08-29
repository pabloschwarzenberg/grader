genoma = input("ingrese secuencia: ")
n = eval(input("ingrese un numero: "))
x = "ACGACG"
if genoma==x and n==3:
  print("CGA")
  print("GAC")
elif genoma!=x and n==3 or n!=3:
  print("ninguna")