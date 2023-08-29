def jerigonzo(string):
    l=string
    s=list(l)
    for i in range(len(s)):
    
      if s[i]=="a":
          s[i]="apa"
          u="".join(s)
        
      elif s[i]=="e":
          s[i]="epe"
          u="".join(s)
        
      elif s[i]=="i":
          s[i]="ipi"
          u="".join(s)
        
      elif s[i]=="o":
          s[i]="opo"
          u="".join(s)
        
      elif s[i]=="u":
          s[i]="upu"
          u="".join(s)
        
    
    return(u)        
           
    

if __name__ == "__main__":
    pass
         