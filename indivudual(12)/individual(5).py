import numpy as np

import matplotlib.pyplot as plt

# Данные о расходах компании на различные виды рекламы за квартал (примерные данные)
ad_types = np.array(['TV', 'Radio', 'Online', 'Print', 'Outdoor'])
expenses = np.array([50000, 15000, 30000, 10000, 5000])  # Примерные данные о расходах

# Общая сумма расходов
total_expenses = np.sum(expenses)

# Процентная доля расходов на каждый вид рекламы
percentages = (expenses / total_expenses) * 100

# Построение круговой диаграммы
plt.figure(figsize=(10, 6))
plt.pie(expenses, labels=ad_types, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, wedgeprops={'edgecolor': 'black'})

# Название диаграммы
plt.title('Доля расходов на каждый вид рекламы за квартал', fontsize=16, fontweight='bold')

plt.show()