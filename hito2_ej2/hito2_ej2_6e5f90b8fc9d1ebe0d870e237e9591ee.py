hebraA = input("Hebra: ").upper()

i=0
c=0


while i< len(hebraA) : 
      if hebraA[i]== "A" or hebraA[i]== "T"   or hebraA[i]== "C" or hebraA[i]== "G" :
          c+=1
     
      if c==len(hebraA):
         print("Secuencia Correcta") 
      else:
         print("Secuancia Incorrecta") 
      i+=1    