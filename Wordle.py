from wonderwords import RandomWord

w=RandomWord()
word=w.word(word_min_length=5,word_max_length=5).strip().lower()
i=1
while i<7:
    k=''
    while len(k)!=5:
        k=input("Input a valid 5 letter word: ").strip().lower()
    output=""
    if word==k:
        print("You guessed the word in "+ str(i) +" tries!")
        break
    for j in range(0,5):
        if k[j] == word[j]:
            output+=k[j]+" is green. "
        elif k[j] in word[j]:
            output+=k[j]+" is yellow. "
        else:
            output+=k[j]+" is grey. "
    print(output)
    output=''
    i+=1