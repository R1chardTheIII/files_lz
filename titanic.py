import matplotlib.pyplot as plt
import pandas

f = pandas.read_parquet('titanic.parquet')    #открываем исходный файл
f.to_csv('titanic.csv')    #преобразуем его в cvs

f_1 = pd.read_csv('titanic.csv')    #создаем файл 
z = file_1.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

s = a.div(a.sum(axis=1), axis=0) * 100 
s.plot(kind='bar', stacked=True)

plt.title('Выживаемость пассажиров от класса')    #задаем данные гистограммы и оси
plt.xlabel('Класс') 
plt.ylabel('% выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()

plt.show()    #показ гистограммы 
