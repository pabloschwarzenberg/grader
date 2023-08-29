import random

index = -1
infi = ("python","jumble","hide","mama")

word = random.choice(infi)
word_len = len(word)
guess = ""
attempt = 0
enter = ""
print(word)
temp = "_" * word_len

print("tt The word chosen by computer contain", word_len,"letters.")
print("t  Tap any letter to check if this letter is in computer word.n")
print("t You got 5 attempts to check if tapped letter is in computer word.n")
print("tttt GOOD LUCK!!!nnnn")

for i in range(0, 5):
attempt +=1
guess = input("Attempt no. "+str(attempt)+":")
if guess in word and guess != enter:
for i in range(0, word_len):
if guess == word[i]:
temp = temp[:i] + guess +temp[i+1:]
print("yesn" + temp)
if guess not in word:
print("no")
if "_" not in temp:
print("tt*********** Congratulation!! You guess the word *************")
break
elif attempt == 5:
guess = input("And the word is:")
if guess == word:

print("tt*********** Congratulation!! You guess the word *************")
else:
print("tt*********** WRONG!! Shame on you *************")