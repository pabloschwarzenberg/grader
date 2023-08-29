# completa el código de la función
def rot13(palabra):
    L1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    L2=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"]
    J=0
    T=""
    while J<len(palabra):
        I=0        
        while I<len(L1):
            if palabra[J]==L1[I]:
                T+=L2[I]
        
        
            I=I+1
        J=J+1
    return T     
                
                
        
    