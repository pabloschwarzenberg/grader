def amigos(a,b):
  if a!=b:
    def divisores(num):
      acum=[]
      suma=0
      for divisor in range(1,num+1):
          if (num % divisor) == 0 :
            acum.append(divisor)
            suma=suma+divisor
      return acum 
    cant1=divisores(a)
    cant2=divisores(b)
    master_set = set(cant1)
    list1 = [x for x in cant2 if x not in master_set]
    list2 = [x for x in master_set if x not in cant2]
    suma1 = 0
    for i in list1:
        suma1 = suma1 + i
    suma2 = 0
    for j in list2:
        suma2 = suma2 + j      
    if suma1==suma2:
      return True
    else:
      return False
  else:
    return False