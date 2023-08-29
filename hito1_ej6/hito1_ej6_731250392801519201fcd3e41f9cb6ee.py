a=int(input())
b=int(input())
c=int(input())

if a < b and b < c or a == b and c > a or b == c and b < a:
   print(a ,",", b ,",", c)
else:
     if a < c and c < b or a == c and b > a:
        print (a ,",", c ,",", b)
     else:
           if b < a and a < c or a == c and b < a:
              print(b ,",", a ,",", c)
           else:
                 if b < c and c < a or b == c and b > a:
                    print(b ,",", c ,",", a)
                 else:
                       if c < a and a < b or a == b and c < a:
                          print(c ,",", a ,",", b)

                                            
                                             
                           
                  