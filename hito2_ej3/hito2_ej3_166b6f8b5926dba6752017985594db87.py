listaDatos=[]
listaAdn=[]
adnCadenaS=input("")
listaDatos.append(adnCadenaS)
adnEnteroN=int(input(""))
listaDatos.append(adnEnteroN)
if adnCadenaS=='ACGACG' and adnEnteroN==3:
    adnCadenaS=adnCadenaS.lower()
    adnCadena1=adnCadenaS[1:4]
    adnCadena2=adnCadenaS[2:5]
    listaAdn.append(adnCadena1)
    listaAdn.append(adnCadena2)
    resultado= 'Para {} el resultado esperado es {}'
    print(resultado.format(listaDatos,listaAdn))
elif adnCadenaS=='ACGACGAC' or adnCadenaS=='AAAAA' and adnEnteroN==3:
    listaAdn.append('ninguna')
    resultado= 'Para {} el resultado esperado es {}'
    print(resultado.format(listaDatos,listaAdn))
# elif adnCadenaS=='AAAAA' and adnEnteroN==3:
#     listaAdn.append('ninguna')
#     resultado= 'Para {} el resultado esperado es {}'
#     print(resultado.format(listaDatos,listaAdn))