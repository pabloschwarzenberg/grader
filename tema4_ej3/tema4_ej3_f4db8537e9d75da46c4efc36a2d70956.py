def jerigonzo(string):
  l1=["a","e","i","o","u"]
  l2=["apa","epe","ipi","opo","upu"]
  s=list(string)
  i=0
  j=0
  while i<len(s):
    if s[i]==l1[j]:
       s[i]=l2[j]
    if j<4:
      j=j+1
    if j==4:
      i=i+1
      j=0
  string="".join(s)
  return string

if __name__ == "__main__":
    pass
         