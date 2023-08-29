def float_bin(number, places = 3): 
  
    
    
    whole, dec = str(number).split(".") 
  
    
    
    whole = int(whole) 
    dec = int (dec) 
  
    
    
    
    res = bin(whole).lstrip("0b") + "."
  
    
    
    for x in range(places): 
  
        
        
        
        whole, dec = str((decimal_converter(dec)) * 2).split(".") 
  
        
        
        dec = int(dec) 
  
        
        
        res += whole 
  
    return res 
  
def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num 
  
  

  
p = int(input("Enter the number of decimal places of the result : \n")) 
  
 
         