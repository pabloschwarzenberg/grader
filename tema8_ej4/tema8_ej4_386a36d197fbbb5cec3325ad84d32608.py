def rot13(palabra):
   i=['a','b','c','d','e','f','g','h','i','j','k','l','m']
   i2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
   p=""
   for j in range(0, len(palabra)):
       for x in range(0,13):
           if(palabra[j]==i[x]):
               p=p+i2[x]
           if(palabra[j]==i2[x]):
                p=p+i[x]
   return(p)

           