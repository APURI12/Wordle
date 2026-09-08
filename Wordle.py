from wonderwords import RandomWord

w=RandomWord
word=w.word(word_min_length=5,word_max_length=5)

i=0
while i<6:
    k=''
    while len(k)!=5:
        k=input("Input a valid 5 letter word: ")
    for j in range(0,5):
        if k[j] in word:
            print(k[j]+" is in the word.")
    i+=1