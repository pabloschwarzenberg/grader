def jerigonzo(b):
    c=""
    i=0
    while i<len(b):
       c=c+b[i]
       if b[i]=="A" or b[i]=="E" or b[i]=="I" or b[i]=="O" or b[i]=="U" or b[i]=="a" or b[i]=="e" or b[i]=="i" or b[i]=="o" or b[i]=="u":
           c=c+"p"+b[i]
       i=i+1
    return c