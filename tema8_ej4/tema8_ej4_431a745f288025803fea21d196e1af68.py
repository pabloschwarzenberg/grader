def rot13(palabra):
    abecedario = 'a,b,c,d,e,f,g,h,i,j,k,l,m'
    abecedario2 = 'n,o,p,q,r,s,t,u,v,w,x,y,z'
    cifrado = dict(zip(abecedario + abecedario2, abecedario2 + abecedario))
    return ''.join(cifrado.get(x.lower(), x) for x in palabra)
 
if __name__=="__main__":
    palabra=input("su palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("su palabra es: ",resultado)
