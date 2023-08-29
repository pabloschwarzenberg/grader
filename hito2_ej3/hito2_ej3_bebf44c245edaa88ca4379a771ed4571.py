string=input("Ingrese cadena de ADN: ")
n=int(input("Ingrese entero: "))

respuesta=[]

if len(string)%n==0:
  i=0
  while i<len(string):
    if string.count(string[i:i+n])==1:
      respuesta.append(string[i:i+n])
      i+=1
    else:
      i+=1
  
  print(respuesta)

else:
  print("Ninguna")