import matplotlib    #импортируем библиотеки
import docx
i = str(input())    #элемент, который должна найти программа
words = {}

f = open('lion.docx').read()    #открывает и читает файл
doc = docx.Document(f)    #программа читает текст их файла

txt = f.split()
for i in txt:    #
    if i in words:
        words[i] += 1
    else:
        words.update({i:1})

print(words)            
