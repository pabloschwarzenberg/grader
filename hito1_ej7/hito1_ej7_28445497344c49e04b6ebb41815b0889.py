dia=int(input())
mes=int(input())
lista=["Capricornio","Acuario","Piscis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpio","Sagitario"]
if dia<22 :
    mes=mes-1
print(lista[mes%12])