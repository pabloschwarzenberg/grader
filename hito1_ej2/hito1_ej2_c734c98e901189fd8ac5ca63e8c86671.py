#Contestador de celular
n=int(input('Ingrese numero telefonico:'))
h=int(input('Ingrese hora de la llamada:'))
a=n-n//1000*1000
if 0<=h<=7:
    print('Contestar')
elif h<14 and a==909:
    print('Contestar')
elif h<14:
    print('No contestar')
elif 16<h<20 and n>87799999 :
    print('Contestar')
elif 16<h<20 and n<87700000:
    print('Contestar')
elif 16<h<20 and 87700000<=n<=87799999:
    print('No contestar')
elif h>19:
    print('No contestar')

     