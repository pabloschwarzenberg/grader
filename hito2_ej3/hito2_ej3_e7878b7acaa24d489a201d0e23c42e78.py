print("Ingrese secuencia de ADN:")
str_adn=input("")
print("Ingrese largo:")
contador=int(input())
contador2=0
lista=[]
while contador<=len(str_adn):
    lista.append(str_adn[contador2:contador])
    contador+=1
    contador2+=1
for i in range(0,len(lista)):
    if lista.count(lista[i])==1:
               print(lista[i])
    else:
      print("ninguna")