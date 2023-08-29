def jerigonzo(string):
    string_1=list(string)
    s=""
    vocales=['a','e','i','o','u']
    for i in range(0,len(string_1)):
      s=s+string_1[i]
      if string_1[i] in vocales:
         s=s+"p"+string_1[i]
    return s

if __name__ == "__main__":
    string=input()
    print(jerigonzo(string))
         