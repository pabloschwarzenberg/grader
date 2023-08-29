#Conversión de Decimal a Binario
def binario(bina):
  binario = ""
  while bina // 2 != 0:
    binario = str(bina%2)+binario
    bina = bina//2
  return str(bina) + binario
numero = int(input("numero a binario: "))
print("resultado=",binario(numero))