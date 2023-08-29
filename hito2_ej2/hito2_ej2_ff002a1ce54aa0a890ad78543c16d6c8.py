palabra=input("ingresa una palabra: ")
palabra=palabra.lower()
i=0
ver=0
fal=1
while i<len(palabra):
   print(palabra[i])
   if palabra[i]==("A")and("C")and("T")and("G"):
      ver=ver-1
      print("secuencia correcta")
   else:
      print("secuencia incorrecta")
      fal=fal+1
   i=i+1
