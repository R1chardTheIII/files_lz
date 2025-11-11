import matplotlib.pyplot as plt
import docx

doc = docx.Document('lion.docx')    #программа открывает документ
txt = []
letters = {}

w = str(input(''))
l = str(input(''))

for pr in doc.paragraphs:    
    txt.append(pr.txt)

txt = txt.lower()
total_words = txt.count(w)
p_1 = ((total_words / len(txt))*100)
# ------------------------------------------------------------------------
for i in txt:    #цикл для нахождения букв в тексте
    for z in i:
        if z in l:
            l[z] += 1
        
        else:
            l.update({z:1})
# ------------------------------------------------------------------------
keys = list(l.keys())    #создаем оси для графика
values = list(l.values())
plt.bar(keys, values)     #создаем график
# ------------------------------------------------------------------------
plt.xlabel("Буквы")    
plt.ylabel("Количество")
plt.title("Гистограмма количества букв")
plt.show()    #показ графика
# ------------------------------------------------------------------------
table = docx.add_table(rows = 2, cols = 3)    #создаем таблицу
table.cell(0, 0).txt = "Слово"
table.cell(0, 1).txt = "Частота встречи, раз"
table.cell(0, 2).txt = "Частота встречи в процентах"
table.cell(1, 0).txt = str(w)
table.cell(1, 1).txt = str(total_words)
table.cell(1, 2).txt = str(p_1)
