def numero_perfecto(a):
      suma_a=0
      for ia in range(1,a) :
         ra=a%ia
         if ra==0:
            suma_a=suma_a + ia
      if suma_a==a:
          return True
      else:
          return False
             
              
              
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    
           