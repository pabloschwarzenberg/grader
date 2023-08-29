#Conversión de Decimal a Binario

def binario (numero):
   b = ''
   while numero // 2 != 0:
      b = str(numero % 2) + b
      numero = numero // 2
   return str(numero) + b
   
c = int(input("Ingrese un numero cualquiera"))
print("resultado=%s" % (binario(c)))