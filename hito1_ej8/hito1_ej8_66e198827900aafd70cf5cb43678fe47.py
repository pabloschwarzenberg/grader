#Descomponer un número
numero=int(input("ingrese un numero de hasta 4 digitos:"))
um=numero//1000
ce=(numero-(um*1000))//100
de=(numero-(um*1000)-(ce*100))//10
en=(numero-(um*1000)-(ce*100)-(de*10))
if(um==0 and ce==0 and de==0):
    print(en,"U+")
elif(um==0 and ce==0):
    print(de,"D+", en,"U+")
elif(um==0):
    print(ce,"C+",de,"D+",en,"U+")
else:
    print(um,"M+",ce,"C+",de,"D+",en,"U+")