letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def rot13(palabra):
    palabra=list(palabra)

    
    for i in range(0,len(palabra)):                  
      j=0  
      while j<(len(letras)):
       if palabra[i] == letras[j]:
          if j<=12:
              palabra[i]=letras[j+13]
              break
          elif j>=13:
              palabra[i]=letras[j-13]
              break
          
       else:
           j=j+1    

    palabra=''.join(palabra)
    return palabra
palabra=input('Ingrese palabra a codificar: ')
print(rot13(palabra))