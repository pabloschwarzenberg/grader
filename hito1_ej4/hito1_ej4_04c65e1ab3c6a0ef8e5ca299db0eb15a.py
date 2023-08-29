#Conversión de Decimal a Binario
nom = int(input("Ingrese número a pasar a binario: "))
bin = ""
while nom != 0:
  potencia1 = 1
  potencia2 = 2
  n = 0

  while potencia1 <= nom:
    if potencia1 <= nom and potencia2 > nom:
      break

    potencia1 = potencia1 * 2 
    potencia2 = potencia1 * 2 
    n+=1

  while n >= 0:
    pot = 2**n
    
    if nom >= pot:
      bin += "1"
      nom -= pot
      
    elif nom < pot:
      bin += "0"
    n-=1
print(bin)