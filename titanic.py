import matplotlib.pyplot as plt
import pandas as pd
# --------------------------------------------------------------
f = pd.read_parquet('titanic.parquet')    #открываем исходный файл
f.to_csv('titanic.csv')    #преобразуем его в cvs
# --------------------------------------------------------------
f_1 = pd.read_csv('titanic.csv')    #создаем файл 
z = f_1.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
# --------------------------------------------------------------
surv = z.div(z.sum(axis=1), axis=0) * 100 
surv.plot(kind='bar', stacked=True)
# --------------------------------------------------------------
plt.title('Выживаемость пассажиров от класса')    #задаем данные гистограммы и оси
plt.xlabel('Класс') 
plt.ylabel('Процент выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()
plt.show()    #показ гистограммы 
