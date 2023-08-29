#Ordenar tres números
def validanum(dato,tipo):
    if tipo !='int' and tipo !='float':
        return 0 #error
    else:
        try:
            if tipo == 'int':
                dato=int(dato)
            else:
                dato=float(dato)
            return 1 #ok
        except:
            return 0 #error
 
norg=0
p=1
lista=[]
vlr_tmp=0
texto= ' '
temp=0
rep=' '
while p>0:
    print "Organizador de numeros"   '
    while True:
        try:
            norg=raw_input('Cuantos numeros desea organizar? \n->')
            norg=int(norg)
            break
        except:
            print 'Valor incorrecto. Vuelva a intentarlo.'
 
    for i in range (1,norg+1):
        vlr_tmp=raw_input('Digite el campo numero '+ str(i) + ': ')
        while validanum (vlr_tmp,'float')==0:
            vlr_tmp=raw_input('ERROR, campo no numerico.\nDigite el campo numero '+ str(i) + ': ')
        lista.append(float(vlr_tmp))
    for recorrido in range(1,len(lista)):
        for posicion in range (len(lista)-recorrido):
            if lista[posicion]>lista[posicion+1]:
                temp=lista[posicion]
                lista[posicion]=lista[posicion+1]
                lista[posicion+1]=temp
    print '   \n    '
    print 'Ordenados: ',lista
 
    print '    '
    rep=raw_input('Desea repetir el programa?(si o no) ')
    while rep !='si'and rep !='no':
        rep=raw_input('Valor incorrecto. Vuelva a intentarlo. ')
    if rep=='no':
        print '\nGracias por usar nuestro programa. \n \nDesarrollado por: \n Julian Ceron \n William Ceron'
        break
    elif rep=='si':
        print '\nReiniciando... \n     \n'
        lista=[]
        vlr_tmp=0