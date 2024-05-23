import numpy as np

import matplotlib.pyplot as plt

# Создание двумерного массива с данными о количестве посетителей за две недели (примерные данные)
# Каждая строка представляет неделю, а каждый столбец - день недели (например, Понедельник - Воскресенье)
visitors_data = np.array([
    [120, 150, 180, 200, 220, 250, 300],  # Первая неделя
    [130, 160, 170, 210, 230, 260, 310]   # Вторая неделя
])

days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

# Построение гистограммы
x = np.arange(len(days_of_week))  # Индексы для оси X
width = 0.35  # Ширина столбцов

fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(x - width/2, visitors_data[0], width, label='Неделя 1', color='skyblue', edgecolor='black')
bar2 = ax.bar(x + width/2, visitors_data[1], width, label='Неделя 2', color='salmon', edgecolor='black')

# Добавление подписей к осям и названию диаграммы
ax.set_xlabel('Дни недели')
ax.set_ylabel('Количество посетителей')
ax.set_title('Количество посетителей парка аттракционов за две недели')
ax.set_xticks(x)
ax.set_xticklabels(days_of_week)
ax.legend()

# Добавление значений над столбцами
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bar1)
add_labels(bar2)

plt.show()