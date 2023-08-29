def levenshtein(palab1, palab2):
  res=dict()
  for i in range(len(palab1) + 1):
     res[i]=dict()
     res[i][0]=i
  for i in range(len(palab2) + 1):
     res[0][i] = i
  for i in range(1, len(palab1) + 1):
     for j in range(1, len(palab2) + 1):
        res[i][j] = min(res[i][j-1] + 1, res[i-1][j] + 1, res[i-1][j-1] + (not palab1[i - 1] == palab2[j - 1]))

  a=[]
  a = res[len(palab1)][len(palab2)]
  if a==0:
      return "0D"
  if a>1:
      return "+1"

  if a==1:
      if len(palab1)==len(palab2):
          for i in palab1:
              if i not in palab2:
                  return "1S"
      else:
        return "IB"

if __name__ == "__main__":
    pal1=input("Ingrese palabra 1: ")
    pal2 = input("Ingrese palabra 1: ")
    print(levenshtein(pal1,pal2))