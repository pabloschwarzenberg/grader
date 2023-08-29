#Conversión de Decimal a Binario
numero= int (input("ingrese un numero:"))
lista= ""
resto=0
while numero != 0 :
  resto = numero % 2
  numero= numero//2
  lista=lista+ str (resto)
lista= lista [::-1]
print ("resultado="+ str(lista))