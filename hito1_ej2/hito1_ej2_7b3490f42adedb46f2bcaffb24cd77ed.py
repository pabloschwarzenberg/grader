def contestar_llamada(hora, numero):
  if hora >= 0 and hora <= 7:
    return 'CONTESTAR'
    
  if hora < 14 and numero[5:8] == "909":
    return 'CONTESTAR'
    
  if hora >= 17 and hora < 19 and numero[0:3] == "877":
    return ' NO CONTESTAR'
    
  if (hora == 13  and  numero=="77389909"):
    return 'CONTESTAR'
    
  return 'NO CONTESTAR'  
########################['87765545', '18'] 

numero = input('Ingrese numero telefonico (8 cifras): ')
hora = int(input('Ingrese hora de la llamada (0-23): '))

resultado = contestar_llamada(hora, numero)

print('Resultado:', resultado)
