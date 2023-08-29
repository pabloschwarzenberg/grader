
palabra=input("ingrese la palabra: ")
palabra=palabra.lower()
I=0
letras_malas=0
while I<len(palabra):
    print("i es ",I,"la letra es ",palabra[I])
    if palabra[I]!="a" and palabra[I]!="c" and palabra[I]!= "t" and palabra[I]!="g":
        letras_malas=letras_malas+1
    I=I+1
print(letras_malas)
#igual ==
#mayor >
#menor <
#distinto !=
if letras_malas==0:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
           
    
