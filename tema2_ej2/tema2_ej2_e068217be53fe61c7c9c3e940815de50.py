def amigos(a,b):
      lista_1=[]
      lista_2=[]
      suma1=0
      suma2=0
      Division=0
      Division2=0
      for i in range(1,a):
            Division=a/i
      if (Division%2==0):
            lista_1.append(Division)
            suma1=sum(lista_1)
      primero=suma1
      for i in range(1,b):
            Division2=b/i
      if (Division2%2==0):
            lista_2.append(Division2)
            suma2=sum(lista_2)
      segundo=suma2
      if(a)==(b) or (b)==(a):
            return(False)

      elif (primero==segundo) and (segundo==primero):
            return True
      else:
            return False