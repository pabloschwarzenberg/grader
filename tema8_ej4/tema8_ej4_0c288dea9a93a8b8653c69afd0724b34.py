def rot13(palabra):
   ind=[]
   lis={"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}        
   for i in range (len(palabra)):
      alm=palabra[i]
      ind.append(lis[alm])
   y= "" .join(ind)
   return y