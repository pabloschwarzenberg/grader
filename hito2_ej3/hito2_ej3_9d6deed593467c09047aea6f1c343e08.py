def obtener_substrings(s, n):
  return [s[i:i+n] for i in range(len(s)-n+1)] 
  
 
s = input("Ingrese el string: ")
n = int(input("Ingrese el tamaño del substring: "))
  
substrings = obtener_substrings(s, n)

contador = {}
for sub in substrings:
  if sub in contador:
    contador[sub] += 1
  else:
    contador[sub] = 1

encontrados = False
for sub, count in contador.items():
  if count == 1:
    encontrados = True
    print(sub)
    
if not encontrados:
  print("ninguna")    
    
    
    