def rot13(palabra):
   lista=[]
   for i in palabra:
       if i.isupper():
           equivalent=ord(i)
           if equivalent>77:
               dif=90-equivalent+1
               rec=13-dif
               a=chr(rec+65)
               lista.append(a)
           elif equivalent<=77:
               a=chr(equivalent+13)
               lista.append(a)
       elif i.islower():
           i=i.upper()
           equivalent=ord(i)
           if equivalent>77:
               dif=90-equivalent+1
               rec=13-dif
               a=chr(rec+65)
               a=a.lower()
               lista.append(a)
           elif equivalent<=77:
               a=chr(equivalent+13)
               a=a.lower()
               lista.append(a)
   trad="".join(lista)
   return trad
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)