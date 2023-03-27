with open("speech1.txt",'r') as fp:
    no_of_lines=0
    no_of_word=0
    data=fp.read()

    lines=data.splitlines() # to check how many lines
    words=data.split() # to check how many element
    print(words)
    for line in lines:
        no_of_lines+=1
    for word in words:
        no_of_word+=len(word)
print(no_of_lines)
print(no_of_word)
    

