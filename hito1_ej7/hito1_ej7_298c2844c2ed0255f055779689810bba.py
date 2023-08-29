#Zodiaco
lista = ["aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario","capricornio","acuario","piscis"] 
lista0=[[21,3],[21,4],[22,5],[22,6],[23,7],[23,8],[24,9],[24,10],[23,11],[22,12],[21,1],[20,2]]
listaf=[[20,4],[21,5],[21,6],[22,7],[22,8],[23,9],[23,10],[22,11],[21,12],[20,1],[19,2],[20,3]]
dia=int(input("ingrese su día de nacimiento:"))
mes=int(input("ingrese su mes de nacimiento:"))
i=0
for i in range(0,len(lista0)):
     if mes == lista0[i][1]:
         if dia >= lista0[i][0] and dia<=31:
             print(lista[i])
     if mes == listaf[i][1]:
         if dia <= listaf[i][0] and dia>=1:
              print(lista[i])