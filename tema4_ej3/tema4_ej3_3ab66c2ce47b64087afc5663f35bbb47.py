def jerigonzo(s):
    p=""
    for i in s:
      if i=="a":
        p=p+i+"pa"
      elif i=="e":
        p=p+i+"pe"
      elif i=="i":
        p=p+i+"pi"
      elif i=="o":
        p=p+i+"po"
      elif i=="u":
        p=p+i+"pu"
      else:
        p+=i
    return p
        
        

