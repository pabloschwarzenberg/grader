def jerigonzo(a):   
    i=0  
    jerigonz=""
    while i<len(a):          
      if "a"==a[i] or "o"==a[i] or "i"==a[i] or "e"==a[i] or "u"==a[i]:
          jerigonz+=a[i]+"p"+a[i]   

      else:
          jerigonz+=a[i]
      i+=1
 
    
    return jerigonz

if __name__ == "__main__":
    string=input("Ingresa palabra para transformar a jerigonzo:")
    print (jerigonzo(string))
         