pt=float(input("Ingrese nota de Tareas :"))
pi=float(input("Ingrese nota de Interrogantes :"))
en=float(input("Ingrese nota de Examen :"))
pp=float(input("Ingrese nota de Presentacion :"))

notaPt=pt*0.3
notaPi=pi*0.3
notaEn=en*0.3
notaPp=pp*0.1

promedioFinal=notaPt+notaPi+notaEn+notaPp
print(round(promedioFinal,2))