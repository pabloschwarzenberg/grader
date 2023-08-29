adn=input()
n=int(input())
strings=[]
for i in range(len(adn)-n+1):
    strings.append(adn[i:i+n])
none=True
for codon in strings:
    cmod=strings.copy()
    cmod.remove(codon)
    if codon not in cmod:
        print(codon)
        none=False
if none==True:
  print("ninguna")