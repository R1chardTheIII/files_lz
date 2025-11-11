import matplotlib.pyplot as plt
import pandas
# ------------------------------------------------------
file = pandas.read_parquet('titanic.parquet')    #открываем исходный файл
file.to_csv('titanic.csv')    #преобразуем его в cvs
# ------------------------------------------------------
file_1 = pd.read_csv('titanic.csv')    #создаем файл 
a = file_1.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
# ------------------------------------------------------
surv = a.div(a.sum(axis=1), axis=0) * 100 
surv.plot(kind='bar', stacked=True)
# ------------------------------------------------------
plt.title('Выживаемость пассажиров от класса')    #задаем данные гистограммы и оси
plt.xlabel('Класс') 
plt.ylabel('Процент выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()
plt.show()    #показ гистограммы 
