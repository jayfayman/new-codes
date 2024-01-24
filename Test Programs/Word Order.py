words_length = int(input("Enter the number of words you want to enter: "))
words = []
distinct_words = 0
word_occurences = []
matched_words = []

for i in range (words_length):
    words.append(input())

for j in range (len(words)):
    if words.count(words[j]) == 1:
        distinct_words +=1
        word_occurences.insert(j,1)
    else:
        if words[j] in matched_words:
            continue
        else:
            matched_words.append(words[j])
            copies = words.count(words[j])
            word_occurences.insert(j,copies)
            distinct_words +=1         

print (distinct_words)
print (*word_occurences,sep=' ')        