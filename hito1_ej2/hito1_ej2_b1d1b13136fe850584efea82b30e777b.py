#Contestador de celular
 tel = int(input('Ingrese numero telefonico'))
 hora = int(input('Ingrese hora de la llamada'))
 
tel = str(tel) 
   if hora >= 0 and hora<= 7:
     print('CONTESTAR')
   elif hora < 14 and tel[5:8] == '909':
     print('CONTESTAR')
   elif hora >= 17 and hora<= 19 and tel[0:3] != '877':
     print('CONTESTAR')
   else
     print('NO CONTESTAR')