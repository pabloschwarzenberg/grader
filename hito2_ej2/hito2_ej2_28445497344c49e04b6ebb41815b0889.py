frase=input()
frase=frase.upper()
letras="ACTG"
a=0
for letra in frase:
   if not letra in letras:
       a=1
if a==1:
    print("secuencia incorrecta")
else:
    print("secuencia correcta")