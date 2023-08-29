palabra=input("ingresa una palabra:")
palabra=palabra.lower()

I=0
cuenta=0
while I<len(palabra):
    if palabra[I]=="a" or palabra[I]=="c" or palabra[I]=="t" or palabra[I]=="g":
       print(palabra[I])
       cuenta=cuenta+1
  
    I=I+1
if cuenta==len(palabra):
     print("secuencia correcta")
else:
    print("secuencia incorrecta")