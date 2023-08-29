      ##Alineamiento de Secuencias
peptidicoseñal="MALTLLATLLLCIAFT"
print(peptidicoseñal)

print("la secuencia de Aminoacidos del peptidico-señal es:",peptidicoseñal)

peptidicoseñal=peptidicoseñal.lower()
print(peptidicoseñal)

peptidicoseñal=peptidicoseñal.upper()
print(peptidicoseñal)

secuencia_ADN="GCTAATGATGCCCGATGCCCTAAAGCTAGGGCTAGTT"
secuencia_ARN=secuencia_ADN.replace("T","U")
print("la secuencia de ADN es:",secuencia_ADN)
print("la secuencia de ARN es:",secuencia_ARN)

contadorcitocinas=secuencia_ADN.count("C")
contadorguaninas=secuencia_ADN.count("G")
contadoradenina=secuencia_ADN.count("A")
contadortimina=secuencia_ADN.count("T")
print("Cantidad de Citocinas de la secuencia de ADN",contadorcitocinas)
print("Cantidad de Guanina de la secuencia de ADN",contadorguaninas)
print("Cantidad de Adenina de la secuencia de ADN",contadoradenina)
print("Cantidad de Timina de la secuencia de ADN",contadortimina)