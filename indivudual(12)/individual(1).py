import numpy as np

import matplotlib.pyplot as plt

# Создание вектора размера 10 и заполнение его значениями от 50 до 59
vector = np.arange(50, 60)

# Перемешивание значений вектора случайным образом
np.random.shuffle(vector)

# Вывод результата
print("Перемешанный вектор:", vector)

# Визуализация результата
plt.figure(figsize=(10, 6))
plt.bar(range(1, 11), vector, color='skyblue', edgecolor='black')
plt.xlabel('Индекс элемента')
plt.ylabel('Значение')
plt.title('Перемешанный вектор значений от 50 до 59')
plt.grid(True)
plt.show()