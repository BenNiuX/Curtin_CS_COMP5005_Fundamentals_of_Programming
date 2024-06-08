import sys
punctuation = '~!@#$%^&*()_+{}|:"<>?`=[]\\;\',./'
if len(sys.argv) <2 :
    filename = 'grimm.txt'
else:
    filename = sys.argv[1]
book = open(filename, encoding='utf-8-sig').read()
bookP = book.translate(str.maketrans('','',punctuation))
words = bookP.lower().split()
print(len(words))
print(words[:10])

wordfreq = {}
for word in words:
    if word not in wordfreq:
        wordfreq[word] = 0
    wordfreq[word] += 1

print(len(wordfreq))
print(wordfreq)