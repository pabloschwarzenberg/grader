def suma_divisores (numero):
       RES1 = 1
       for i in range (2,numero):
              if numero % i == 0:
                     RES1 = RES1 + i

       if numero == 1:
              return (numero - 1 , False)

       elif RES1 == 1:
              return (RES1 , True)
       
       else : 
              return (RES1 , False)       
             

 
if __name__ == "__main__":

       TEST = suma_divisores (1)
       print (TEST)
           