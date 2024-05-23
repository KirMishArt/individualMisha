import numpy as np

import matplotlib.pyplot as plt

# Создание матрицы размера 4x4 и заполнение ее случайными значениями от 1 до 10
matrix = np.random.randint(1, 11, size=(4, 4))
print("Исходная матрица:")
print(matrix)

# Нахождение среднего значения элементов в каждой строке
row_means = np.mean(matrix, axis=1)
print("\nСредние значения по строкам:")
print(row_means)

# Добавление среднего значения в конец каждой строки
extended_matrix = np.hstack((matrix, row_means.reshape(-1, 1)))
print("\nМатрица с добавленными средними значениями по строкам:")
print(extended_matrix)

# Визуализация данных
plt.figure(figsize=(12, 6))

# Построение линий для каждой строки матрицы
for i in range(matrix.shape[0]):
    plt.plot(np.arange(1, 6), extended_matrix[i], marker='o', linestyle='-', label=f'Строка {i+1}')

# Название диаграммы и подписи к осям
plt.title('Значения и средние значения по строкам матрицы 4x4', fontsize=16, fontweight='bold')
plt.xlabel('Индекс элемента')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()