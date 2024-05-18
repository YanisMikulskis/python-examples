# Заполнение матрицы по спирали
# Эта классическая задача часто встречается на собеседованиях и олимпиадах. Рассмотрим несколько способов решения
# на Python.На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером
# n х m, заполнив ее по спирали числами от 1 до n x m. Спираль начинается в левом верхнем углу и закручивается по часовой
# стрелке.
# Пример ввода:
#
# 7 6
#
# 1  2  3  4  5  6
# 22 23 24 25 26 7
# 21 36 37 38 27 8
# 20 35 42 39 28 9
# 19 34 41 40 29 10
# 18 33 32 31 30 11
# 17 16 15 14 13 12

# решение

n = int(input('Введите число n: '))  # строки
m = int(input('Введите число m: '))  # столбцы

class Spiral:
    def __init__(self, m, n):
        self.n_Copy = n
        self.m_Copy = m
        self.line = 1
        self.column = 1
        self.start_vertical = 1
        self.start_horiz = 1
        self.start = 0
        self.results = []
        self.horiz = True
        self.vertical = False
        self.border = self.m_Copy
        self.step_column, self.step_line = 1, 1
        self.start_column, self.start_line = 1, 1
        self.places = [[[i, j] for j in range(1, self.m_Copy + 1)] for i in range(1, self.n_Copy + 1)]

    def setting_order(self):
        for _ in range(self.n_Copy + self.m_Copy - 1):
            self.border = self.m_Copy if self.horiz else self.n_Copy
            self.step_column = self.step_column * -1 if len(self.results) == 2 else self.step_column
            if len(self.results) >= 3:
                if self.vertical:
                    self.step_line, self.start_line = self.step_line * -1, self.start_line + 1
                    self.start = self.start_line - 1
                elif self.horiz:
                    self.step_column, self.start_column = self.step_column * -1, self.start_column + 1
                    self.start = self.start_column - 1
            border_list = []
            for i in range(self.start, self.border - 1):
                self.column = self.column + self.step_column if self.horiz else self.column
                self.line = self.line + self.step_line if self.vertical else self.line
                border_list.append([self.line, self.column])

            border_list.insert(0, [1, 1]) if not len(self.results) else ...
            self.results.append(border_list)
            self.horiz, self.vertical = self.vertical, self.horiz

    def merger(self):
        results_all = [j for i in self.results for j in i]
        test_numbers = list(zip(list(range(1, self.m_Copy * self.n_Copy + 1)), results_all))
        places = [j for i in self.places for j in i]
        places_copy = places.copy()

        for item in test_numbers:
            for elem in places_copy:
                if item[1] == elem:
                    places_copy[places_copy.index(elem)] = item[0]

        self.final_list = [[places_copy.pop(0) for _ in range(m)] for _ in range(n)]

    def result(self):
        for i in self.final_list:
            print(*i)


def main():
    spiral = Spiral(m, n)
    spiral.setting_order()
    spiral.merger()
    spiral.result()

if __name__ == '__main__':
    main()