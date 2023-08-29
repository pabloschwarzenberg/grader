def jerigonzo(string):

  palab = ""
  
  vocales = ["a", "e", "i", "o", "u"]
  
  for i in string:
  
    if i in vocales:
    
      palab += i
      
      palab += "p"
      
      palab += i
      
    else:
    
      palab += i
      
  return palab
      
      
      

         