import numpy as np

import matplotlib.pyplot as plt

# Создание массива с данными о стоимости акций за последний месяц (примерные данные)
# Предположим, что данные о стоимости акций собраны за 30 дней
stock_prices = np.random.uniform(100, 200, size=30)  # Случайные значения от 100 до 200

# Создание массива дней месяца (от 1 до 30)
days = np.arange(1, 31)

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(days, stock_prices, marker='o', linestyle='-', color='b', label='Цена акций')

# Название диаграммы и подписи к осям
plt.title('Изменение цены акций компании за последний месяц', fontsize=16, fontweight='bold')
plt.xlabel('Дни')
plt.ylabel('Цена акций ($)')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()