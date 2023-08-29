def amigos(a,b):
    y= ""
    for x in range(1,a):
         while a%x==0:
             y=str(a%x)+y
             if y==b:
                 return True
             else:
                 return False
             
             