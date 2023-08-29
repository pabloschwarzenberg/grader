decimal = float(input("Ingrese un número decimal: "))
binario = "" 
residuo = 0
while decimal > 0: 
 residuo = decimal % 2 
 if residuo == 1:
  binario = binario + "1"
 if residuo == 0:
  binario = binario + "0"
 decimal = decimal // 2
else:
 reversa = binario[::-1]
 print("Resultado =",reversa)