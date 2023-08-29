string = input("String: ")
n = int(input("n: "))
contador = 0
contadorgral = 0
for i in range (len(string)):
 j = i + 3
 if j <= len(string):
    palabra1 = string[i:i+n]
    contador = 0
    for y in range (len(string)):
      x = y + 3
      if x <= len(string):
        palabra2 = string[y:y+n]
      if palabra1 == palabra2:
         contador += 1
    if contador == 1:
      print(palabra1)
      contadorgral += 1
 if contadorgral == 0:
   print("ninguna")