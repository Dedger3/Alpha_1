import copy
import random

import numpy as np
l1 = [[1,2],["3",4]]
l2 = [[5,"6"],[7,8]]

lis1 = [[1,2]]
lis2 = [[3]]
def funk(ls1, ls2):
    print(f"Двумерный массив 1: {ls1}\nДвумерный массив 2: {ls2}")
    try:
        try:
            for i in range(len(ls1)):
                for j in range(len(ls1[i])):
                    ls1[i][j] = int(ls1[i][j])
        except ValueError:
            print("Ошибка ввода Первой матрицы")

        try:
            for i in range(len(ls2)):
                for j in range(len(ls2[i])):
                    ls2[i][j] = int(ls2[i][j])
        except ValueError:
            print("Ошибка ввода Второй матрицы")
        # change from List[list] to arrays
        ar1_strings = np.array(ls1)
        ar2_strings = np.array(ls2)

        if len(ls1[0]) != len(ls2[0]):
            print("Неверный размер массивов. Количество строк певрого массива должна соответствовать количеству строк другого.")

        result_array = []
        for i in range(len(ar1_strings)): #6
            for j in range(len(ar2_strings)): #12
                for k in range(len(ar1_strings[j])): #2
                    result_array.append(ar1_strings[i][k] * ar2_strings[j][k])

        sum_list = []
        f_array = []
        count_ = 0
        num = 0
        num1 = 0
        for i, j in enumerate(result_array):
            if num == 0:
                count_ += j
                num = 1
                continue
            if num == 1 and num1 == 0:
                count_ += j
                sum_list.append(count_)
                count_ = 0
                num = 0
                num1 = 1
            if num == 1 and num1 == 1:
                count_ += j
                sum_list.append(count_)
                a = copy.deepcopy(sum_list)
                f_array.append(a)
                sum_list.clear()
                count_ = 0
                num = 0
                num1 = 0

        for i in range(len(f_array)):
            print(f_array[i])
        print()

        return f_array
    except:
        print("[[]]\n")

def enter():
    l1.clear()
    l2.clear()
    print("Введите размерность Первого массива через пробел:")
    try:
        count1, count2 = map(int, input().split())
        print("Введите размерность Второго массива через пробел:")
        count3, count4 = map(int, input().split())

        numm = 0
        count_1 = 0
        sum_list1 = []

        for i in range(count1):
            for j in range(count2):
                if numm == 0:
                    count_1 = random.randint(-49, 50)
                    sum_list1.append(count_1)
                    numm = 1
                    continue
                if numm == 1:
                    count_1 = random.randint(-49, 50)
                    sum_list1.append(count_1)
                    a = copy.deepcopy(sum_list1)
                    l1.append(a)
                    sum_list1.clear()
                    numm = 0

        for i in range(count3):
            for j in range(count4):
                if numm == 0:
                    count_1 = random.randint(-49, 50)
                    sum_list1.append(count_1)
                    numm = 1
                    continue
                if numm == 1:
                    count_1 = random.randint(-49, 50)
                    sum_list1.append(count_1)
                    a = copy.deepcopy(sum_list1)
                    l2.append(a)
                    sum_list1.clear()
                    numm = 0
        print("GO")
    except NameError and ValueError:
        print("Ошибка ввода размерности")

if __name__ == '__main__':
    funk(l1, l2)#Example
    funk(lis1, lis2)

    enter()
    funk(l1, l2)