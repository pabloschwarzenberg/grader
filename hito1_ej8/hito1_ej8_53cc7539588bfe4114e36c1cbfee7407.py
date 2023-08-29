numero=int(input("Inserte numero a descomponer"))
numero_s=str(numero)
numero_l=list(numero_s)
if len(numero_s)==1:
    print(numero_s[0],"U")
elif len(numero_s)==2:
    print(numero_s[0],"D",numero_s[1],"U")
elif len(numero_s)==3:
    print(numero_s[0],"C +",numero_s[1],"D +",numero_s[2],"U")
elif len(numero_s)==4:
    print(numero_s[0],"M +",numero_s[1],"C +",numero_s[2],"D +",numero_s[3],"U")