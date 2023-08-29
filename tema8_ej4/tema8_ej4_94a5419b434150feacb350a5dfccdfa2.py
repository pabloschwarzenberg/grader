def rot13(s):
    
    result = ""

    
    for v in s:
       
        c = ord(v)

        if c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        elif c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        
        result += chr(c)

   
    return result

if __name__=="__main__":
    s=input("Ingresa la palabra que quieras encriptar: ")
    resultado=rot13(s)
    print("El resultado es: ",resultado)

