def amigos (a,b):
       RESU1 = 1
       RESU2 = 1
       for i in range (2,a):
              if (a % i == 0):
                     RESU1 = RESU1 + i            
       for x in range (2,b):
              if (b % x == 0):
                     RESU2 = RESU2 + x     
       if RESU1 == b and RESU2 == a:
              return (True)
       else :
              return (False)

TEST = amigos (220,284)
print (TEST)