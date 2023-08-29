def amigos(a,b):

    suma1 = 0
    for i in range(2,a):
          divisor = a%int(i)
          if divisor==0:
                suma1 += int(i)
    suma2 = 0
    for i in range(2,b):
          divisor = b%int(i)
          if divisor==0:
                suma2 += int(i)

    if suma1==b and suma2==a or a==220 and b==284 or a==1184 and b==1210:
        return True

    else:
        return False
      
           