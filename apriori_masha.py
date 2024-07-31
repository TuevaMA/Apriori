"""
Поиск ассоциативных правил. Алгоритм APRIORI
@author: Самойлова
"""
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori  # пакет должен лежать в папке с этой программой
start_time = time.time()
data_df = pd.read_csv('Apriori.csv', sep=',')# исходный файл
print(data_df)
page_visit = data_df.groupby(['userId'])['productId'].unique().to_dict()
#print(page_visit)
page_visit_df = pd.DataFrame(page_visit.values())
#print(page_visit_df )
N = page_visit_df.shape[1]
x = np.array(page_visit_df)
rules_data = []
for row in x:
    t = []
    for i in range(0, N):
        if row[i] != None:
           t.append(row[i])
    rules_data.append(t)
#print(rules_data)
for i in range (len(rules_data)):
    rules_data[i] = list(map(str, rules_data[i]))
# assumptions - This values must be tweaked to get better results
min_support = 0.3
min_confidence = 0.1
min_lift = 1
association_rules = apriori(rules_data, min_support = min_support, min_confidence = min_confidence, min_lift = min_lift)
associetion_results = list(association_rules)
print('asiocianon rule generatian completeted')
print ("РЕЗУЛЬТАТЫ РАБОТЫ apriori")
results = associetion_results
data = []
sup = []
# Расчет поддержки - support - доля набора в общем числе транзакций
print ("Поддержки наборов из 1 продукта:")
for item in results:
    x = list(item.items)
    if (len(x) == 1):   #Отбираем наборы их 1 элементa
        print("ответ: набор продуктов:", x, " поддержка = %.2f" % (100 * item.support), "%")
        data.append(x)
        sup.append(int(100*item.support))  # вероятности в процентах
print ("Результаты по наборам из 1 продукта:")
print (data)
print ("Соответственно поддержки в процентах:")
print (sup)
data1 = data #Для диаграммы
sup1 = sup  #Для диаграммы
print ("Поддержки наборов из 2 продуктов:")
data = []
sup = []
for item in results:
    x = list(item.items)
    if (len(x) == 2):   #Отбираем наборы их двух элементов
        print("ответ: набор продуктов:", x, " поддержка = %.2f" % (100 * item.support), "%")
        data.append(x)
        sup.append(int(100*item.support))  # вероятности в процентах
print ("Результаты по наборам из 2 продуктов:")
print (data)
print ("Соответственно поддержки в процентах:")
print (sup)
data2 = data #Для диаграммы
sup2 = sup  #Для диаграммы
print ("Поддержки наборов из 3 продуктов:")
data = []
sup = []
for item in results:
    x = list(item.items)
    if (len(x) == 3):   #Отбираем наборы из трех элементов
        print("ответ: набор продуктов:", x, " поддержка = %.2f" % (100 * item.support), "%")
        data.append(x)
        sup.append(int(100*item.support))  # вероятности в процентах
print ("Результаты по наборам из 3 продуктов:")
print (data)
print ("Соответственно поддержки в процентах:")
print (sup)
print("-— %s seconds —-" % (time.time() - start_time))

#вывод графиков
# Для 3 продуктов
x0 = [x[0] for x in data]
x1 = [x[1] for x in data]
x2 = [x[2] for x in data]
for i in range(0, len(x0)):
    x0[i] = x0[i] + x1[i] + x2[i]
plt.figure(1)
plt.rcParams["figure.figsize"] = (100,150) # высота, ширина картинки
x = range(len(x0))
plt.xticks(x, x0)
width = 0.8
plt.bar(x,sup, width, color='g') #b - Синяя
plt.xlabel('Рекомендуемые покупки:   номера продуктов ')
plt.ylabel('Поддержка (вероятность) покупки %')
plt.title('Поиск ассоциативных правил ')
plt.show()
# Для 2 продуктов
x0 = [x[0] for x in data2]
x1 = [x[1] for x in data2]
for i in range(0, len(x0)):
    x0[i] = x0[i] + x1[i]
plt.figure(1)
plt.rcParams["figure.figsize"] = (100,150) # высота, ширина картинки
x = range(len(x0))
plt.xticks(x, x0)
width = 0.8
plt.bar(x,sup2, width, color='r') #b - Синяя
plt.xlabel('Рекомендуемые покупки:   номера продуктов ')
plt.ylabel('Поддержка (вероятность) покупки %')
plt.title('Поиск ассоциативных правил ')
plt.show()
# Для 1 продукта
x0 = [x[0] for x in data1]
for i in range(0, len(x0)):
    x0[i] = x0[i]
plt.figure(1)
plt.rcParams["figure.figsize"] = (100,550) # высота, ширина картинки
x = range(len(x0))
plt.xticks(x, x0)
width = 0.8
plt.bar(x,sup1, width, color='b') #b - Синяя
plt.xlabel('Рекомендуемые покупки:   номер продукта ')
plt.ylabel('Поддержка (вероятность) покупки %')
plt.title('Поиск ассоциативных правил')
plt.show()

