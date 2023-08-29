def jerigonzo(string):
    string=list(string)
    vocales=["a","e","i","o","u"]
    jerigonzo=["apa","epe","ipi","opo","upu"]
    i=0
    j=0
    while i<len(string):
      if string[i]==vocales[j]:
        string[i]=jerigonzo[j]
        j=0
        i=i+1
      elif j<4:
        j=j+1
      elif j==4:
        i=i+1
        j=0
    string="".join(string)
    return string

if __name__ == "__main__":
    pass
         