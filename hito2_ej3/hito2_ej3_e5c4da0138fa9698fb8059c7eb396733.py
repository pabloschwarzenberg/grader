 
def validar_secuencia(string,n):
   string = string.lower()
   if string.count(string[0]) == len(string):
     print ("ninguna")
   else:
     cont = 0
     for i in range(len(string)):
       if string.count(string[i:i+n])==1:
         print (string[i:i+n])
         cont+=1
     if cont == 0:
       print ("ninguna")
 
string=input("")
n=int(input(""))
validar_secuencia(string,n)
