#Zodiaco
lista=["Aries","Tauro","Gemenis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]
lista_Di=[[21,3],[21,4],[22,5],[22,6],[23,7],[23,8],[24,9],[24,10],[23,11],[22,12],[21,1],[20,2]]
lista_F=[[20,4],[21,5],[21,6],[22,7],[22,8],[23,9],[23,10],[22,11],[21,12],[20,1],[19,2],[20,3]]        
dia=int(input("Ingrese dia de nacimiento: "))
mes=int(input("Ingrese el mes de naciminto: "))
i=0
for i in range(0,len(lista_Di)):
        if mes == lista_Di[i][1]:
            if dia >= lista_Di[i][0] and dia<=31:
                print(lista[i])
        if mes == lista_F[i][1]:
            if dia <=lista_F[i][0] and dia>=1:
                print(lista[i])
        