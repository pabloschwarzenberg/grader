#Descomponer un número
contadorM=0
contadorC=0
contadorD=0
contadorU=0
copia=0

numero=int(input("Ingrese un numero de 4 digitos para descomponer:"))
copia=numero
while numero>0:
    if numero>=1000:
        numero=numero-1000
        contadorM=contadorM+1
    elif numero>=100:
        numero=numero-100
        contadorC=contadorC+1
    elif numero>=10:
        numero=numero-10
        contadorD=contadorD+1
    elif numero>=1:
        numero=numero-1
        contadorU=contadorU+1
    print(f"para {copia} se debe imprimir:",end="")
    if contadorM != 0:
      print(f"{contadorM}M",end="+")
    if contadorC != 0:
      print(f"{contadorC}C",end="+")
    if contadorD != 0:
      print(f"{contadorD}D",end="+")
    if contadorU != 0:
      print(f"{contadorU}U")  


      