# completa el código de la función
def amigos(a,b):
     suma1 = 0
     for i in range(1,a):
          if a%i == 0:
            suma1 += i
          else:
              continue
            
     suma2 = 0
     for i in range(1,b):
          if b%i == 0:
            suma2 += i   
          else :
              continue
            
     comprobar = a == suma2 and b == suma1
     return comprobar