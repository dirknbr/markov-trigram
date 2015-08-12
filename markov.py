
#given a text, extract 3-grams and then build frequency of 2-gram->next

import re

f1=open('pg6342.txt','r')

punc='[\.\!\?]'
repl='[\n,;"-]'

alltext=' '.join([line for line in f1])

#remove specials and line break
alltext=re.sub(repl,'',alltext)
#split by punc, ignore decimals, make lower
sentences=[s.lower() for s in re.split(punc,alltext) if s<>''] 

print len(sentences)

trigram={}
max_=0
for s in sentences:
    #split by words
    words=[w for w in s.split(' ') if w<>'']
    if len(words)>2:
        for i in range(0,len(words)-2):
            bigram=(words[i],words[i+1])
            _next=words[i+2]
            if bigram not in trigram:
                trigram[bigram]={}
            if _next not in trigram[bigram]:
                trigram[bigram][_next]=0
            trigram[bigram][_next]+=1 #update
            if trigram[bigram][_next]>max_:
                print bigram,trigram[bigram]
                max_=trigram[bigram][_next]

print len(trigram)

f1.close()
