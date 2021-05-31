import re
import codecs
import regex as re 

f = codecs.open("scrapped_text1.txt", "r", "utf-8")
d = codecs.open("all_tops.txt", "w", "utf-8")
texts=[]

for x in f.read().split():
    mas = ""
    for j in x:
        if j!='':
            j=re.sub(r'[a-zA-z]+', '', j.strip().lower()).replace('  ',' ')
            mas=mas+j
    texts.append(mas)

n=len(texts)
index = 0
for k in range(1,4):
    topics=[]
    p = codecs.open("file{id}.txt".format(id=k),"w","utf-8")
    for i in range(index,n-1):
        if texts[i] != '++++++':       
            topics.append( texts[i] + " " )
        
        mas = ""
        for j in texts[i]:
            if j!='':
                j=re.sub(r'[^\pL\p{Space}]', '', j).replace('  ',' ')
                mas=mas+j
        d.write(mas+" ")
        
        if texts[i+1] == '++++++':
            index = i+1
            break

    for topic in topics:
        for j in topic:
            if re.search(r'[^\pL\p{Space}]', j):
                topic=topic.replace(j,'')
        p.write(topic)
    
        
p.close()
d.close()
f.close()
           

     
    
f.close()

