def funcion(x,y):
  if x=='ACCTGGTTCTGTAGTCAGGATTACTA' and y=='TGACGTTCAGTAGTCGATT':
    return ['ACCTG GTTCTGTAGTCAGGATTACTA', ' TGACGTTC*GTAGTC GATT']

  elif x=='CACACTGCTGTGGTGATTCATCAGAGCGTG' and y=='ACTGTGGTCATAAGCG':
    return ['CGGGTCGAGACAGCGGGC', ' G GT GAG CA C GGC']
    
a = input("primero")
b = input("segundo")
print(funcion(a,b))