#CONTESTADOR AUTOMATICO.

num = input("Ingrese número telefonico : ")
hora = input("Ingrese hora de la llamada : ")
numfin = num[5:8]
numinicio = num[0:3]
numfin = int(numfin)
numinicio = int(numinicio)

#Condiciones para contestar o no.
sw = 0

if hora  < "8":
    sw = "1"

if hora < "15":
        if numfin == 909:
                sw = "1"
        else:
                sw = "0"

else:
     if numfin == 909:
            sw = "1"

if hora >= "17" and hora <= "19":
        if numinicio == 877:
                sw = "1"
        else:
                sw = "0"
        sw = "0"

if hora > "18" and hora < "24" :
    sw = "0"

if sw > "0":
        print ("Resultado : CONTESTAR")
else :
        print ("Resultado : NO CONTESTAR")
      