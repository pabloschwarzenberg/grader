def mcm(a,b,ab):
  if b==0:
    final=ab/a
    return final
  else:
    resta=a%b
    return mcm(b,resta,ab)
    
  
if __name__=="__main__":
    pass
           