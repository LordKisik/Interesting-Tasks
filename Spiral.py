'''Выведите таблицу размером n на n,
   заполненную числами от 1 до n**2
   по спирали, выходящей из левого верхнего угла
   и закрученной по часовой стрелке'''

# (19) Сгенирировали матрицу n на n, заполненную нулями.
# (20) Цикл для перебора индексов рядов(i).
# (21) Цикл для перебора индексов столбцов(j).
# В матрице n на n есть 4 сектора явно отличающихся дуруг от друга:
# 1) i <= j and i + j < n
# 2) i <= j and i + j >= n
# 3) i > j and i + j < n
# 4) i > j and i + j >= n
# (23-44) Внутри каждого из секторов при помощи условий и формул
# считаем и присваиваем элементам матрицы соответствующие им значения.
# (44-45) Выводим матрицу на экран.

n = int(input('Введите n: '))
matrix_n_x_n = [[0] * n for i in range(n)]
for i in range(len(matrix_n_x_n)):
    for j in range(len(matrix_n_x_n)):

        if i <= j and i + j < n:
            if i == 0:
                matrix_n_x_n[i][j] = i + j + 1
            elif i > 0:
                matrix_n_x_n[i][j] = matrix_n_x_n[i - 1][j] - 8 * i + 4 * n + 3

        if i <= j and i + j >= n:
            if j == n - 1:
                matrix_n_x_n[i][j] = i + j + 1
            elif j < n - 1:
                matrix_n_x_n[i][j] = (matrix_n_x_n[i - 1][j + 1]
                                      + 8 * j - 4 * n + 10)

        if i > j and i + j < n:
            if j == 0:
                matrix_n_x_n[i][j] = 4 * n - i - 3
            elif j > 0:
                matrix_n_x_n[i][j] = matrix_n_x_n[i][j - 1] - 8 * j + 4 * n - 3

        if i > j and i + j >= n:
            matrix_n_x_n[i][j] = matrix_n_x_n[i - 1][j] - 8 * i + 4 * n + 1
        print(matrix_n_x_n[i][j], '', end='')
    print()
