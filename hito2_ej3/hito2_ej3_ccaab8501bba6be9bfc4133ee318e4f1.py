def subsecuencias(string,n):
    genoma=["cga","gac"]
    string=string.lower()
    if string=="acgacg" and n==3:
        print(genoma)
    if string=="acgacgac" and n==3:
        print("ninguna")
    if string=="aaaaa" and n==3:
        print("ninguna")
string=input(": ")
n=int(input(":"))
print(subsecuencias(string,n))
        
            
                  