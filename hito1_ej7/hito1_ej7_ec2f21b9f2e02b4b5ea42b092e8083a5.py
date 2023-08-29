lista=['aries','tauro','geminis','cancer','leo','virgo','libra','escorpio','capricornio','acuario','piscis']
lista1=[[21,3],[21,4],[22,5],[22,6],[23,7],[23,8],[24,9],[24,10],[23,11],[22,12],[21,1],[20,2]]
lista2=[[20,4],[21,5],[21,6],[22,7],[22,8],[23,9],[23,10],[22,11],[21,12],[20,1],[19,2],[20,3]]
dia=int(input('ingrese dia de cumpleaños'))
mes=int(input('ingrese mes de cumpleaños'))
i=0
for i in range(0,len(lista1)):
    if mes== lista1[i][1]:
        if dia >= lista1[i][0] and dia<=31:
            print(lista[i])
    if mes == lista2[i][1]:
        if dia<= lista2[i][0] and dia>=1:
            print(lista[i])