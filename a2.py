class fc:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + '-' + self.meaning
f=[]
print("WELCOME TO THE FLASHCARD APPLICATION")
while True:
    word=input("ENTER A WORD: ")
    meaning=input("ENTER THE MEANING: ")
    f.append(fc(word,meaning))
    o=input("DO YOU WANT TO CONTINUE? (Y/N)")
    if o=="N":
        break
print("\nYOUR FLASHCARDS: ")
for i in f:
    print("->", i)

