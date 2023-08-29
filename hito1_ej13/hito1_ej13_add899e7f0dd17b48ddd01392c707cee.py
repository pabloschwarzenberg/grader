#Factores Primos
lista=[]
def primo(num1):

  for x in range(1,num1):
    if (num1%x==0 and x!=num1 and x!=1):
      return False

def lista_primos(num2):

  for x in range(2,num2):
    if primo(x)!=False:
      lista.append(x)
  return lista

def divisible(lista,num3):
  for numero in lista:
    if num3%numero==0:
      factores.append(numero)
  return factores

def factores_x(lista, numero, factores_finales):
  divisibles=[]
  print("Sus factores primos son: ")

  while True:
    salida1=primo(numero)
    if salida1!=False:
      factores_finales.append(salida1)
      break

    else:
      lista_primos(numero)
      divisibles=divisible(lista, numero)

      factores_finales.append(divisibles[len(divisibles)-1])
      numero=numero/divisibles[len(divisibles)-1]
  return factores_finales

factores_finales=[1]
lista=[]
factores=[]
numero=input("Ingrese un numero: ")
print factores_x(lista, numero, factores_finales)