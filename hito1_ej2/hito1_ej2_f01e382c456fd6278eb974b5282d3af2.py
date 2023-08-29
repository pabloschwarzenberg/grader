#Contestador de celular
nt = int(input("Ingrese número telefónico: "))
hl = int(input("Ingrese hora llamada: "))


a = nt % 1000
b = nt // 100000

if hl >= 0 and hl <= 7:
  print("CONTESTAR")
elif hl < 14 and a == 909:
  print("CONTESTAR")
elif hl >= 17 and hl <= 19 and b == 877:
  print("NO CONTESTAR")
elif hl >= 17 and hl <= 19:
  print("CONTESTAR")
elif hl > 19:
  print("NO CONTESTAR")