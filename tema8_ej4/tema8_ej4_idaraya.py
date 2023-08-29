def rot13(palabra):
       ciphertext = '' # init empty string
       for char in palabra: # iterate over string
             code = ord(char)
             if char.isupper(): # uppercase letter
                   code += 13
                   if code > ord('Z'): # wraparound
                       code =code-26
             elif char.islower(): # lowercase letter
                 code += 13
                 if code > ord('z'): # wraparound
                     code =code- 26
             char = chr(code) # convert to char
             ciphertext += char # append
       return ciphertext
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)