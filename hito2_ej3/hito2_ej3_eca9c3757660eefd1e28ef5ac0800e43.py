def subsecuencias(s,n):
    sub1=""
    sub2=""
    
    if len(s)%n==0:
        for letra in s:
            if letra not in sub1:
               sub1+=(letra)
            if letra not in sub2:
                sub2+=(letra)
        
        
        print(str(sub1))
        print(str(sub2))
    if len(s)%n!=0:
       print("ninguna")

strings=input("")
numero=int(input(""))
s=subsecuencias(strings,numero)       

      