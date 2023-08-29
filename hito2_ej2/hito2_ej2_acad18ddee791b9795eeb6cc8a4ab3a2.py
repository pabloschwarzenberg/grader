l1=["a", "t", "c", "g"]

b=input("escribe y te digo si puede ser o no una secuencia de ADN:")
b=b.lower()

c=True

for letra_valida in b:
    if letra_valida in l1:
        continue
    else:
        c= False
        break
    
if c==False:
    print ("secuencia incorrecta")

else:
    print ("secuencia correcta")
    
