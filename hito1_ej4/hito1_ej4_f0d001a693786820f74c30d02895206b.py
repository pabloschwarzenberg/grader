decimal= int(input("ingrese decimal: "))
binario= ""

while decimal > 0: 
if decimal % 2 == 0:
      binario = "0" + binario
else:
binario = "1" + binario
decimal = decimal // 2 
  
print("el numero binario es:", binario)