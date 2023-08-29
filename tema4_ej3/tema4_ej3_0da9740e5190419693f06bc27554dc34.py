def jerigonzo(s):
  p=""
  for x in s:
    if x=="a":
        p=p+x+"pa"
    elif x=="e":
        p=p+x+"pe"
    elif x=="i":
        p=p+x+"pi"
    elif x=="o":
        p=p+x+"po"
    elif x=="u":
        p=p+x+"pu"   
    else:
        p=p+x
        
  return(p)

