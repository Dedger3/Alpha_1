import copy
import random
import numpy as np

l1 = [[1,2],[3,4]]
l2 = [[5,6],[7,8]]

lis1 = [[1,2]]
lis2 = [[3]]

w_mas1 = []
w_mas2 = []

count_list = []

def funk(w_mas1, w_mas2):
    result_array = []
    print(f"Двумерный массив 1: {w_mas1}\nДвумерный массив 2: {w_mas2}")
    try:
        for i in range(len(w_mas1)):  # 2
            for j in range(len(w_mas2)):  # 3
                if j >= 1:
                    continue
                for h in range(len(w_mas2[j])):  # 4
                    sum_mas = 0
                    for k in range(len(w_mas1[i])):  # 3
                        sum_mas += w_mas1[i][k] * w_mas2[k][h]
                        if k == len(w_mas1[i]) - 1:
                            count_list.append(sum_mas)
                            if h == len(w_mas2[j]) - 1:
                                b = copy.deepcopy(count_list)
                                result_array.append(b)
                                count_list.clear()
        fin = np.array(result_array)
        print(fin)

        return fin
    except:
        print("Ошибка ввода: [[]]\n")

def enter():
    try:
        print("Введите размерность Первого массива через пробел (Каждое значение не больше 10 000):")
        count1, count2 = map(int, input().split())
        if count1 >10000 or count2 > 10000:
            print("Вы ввели больше 10 000")
            return

        print("Введите размерность Второго массива через пробел (Каждое значение не больше 10 000):")
        count3, count4 = map(int, input().split())
        if count3 >10000 or count4 > 10000:
            print("Вы ввели больше 10 000")
            return

        # Input funktions
        for i in range(count1):  # 2
            buf_mas = []
            for j in range(count2):  # 3
                if j != count2 - 1:
                    a = random.randint(-10,10)
                    buf_mas.append(a)
                else:
                    a = random.randint(-10,10)
                    buf_mas.append(a)
                    b = copy.deepcopy(buf_mas)
                    w_mas1.append(b)
                    buf_mas.clear()

        # Input funktions
        for i in range(count3):  # 2
            buf_mas = []
            for j in range(count4):  # 3
                if j != count4 - 1:
                    a = random.randint(-10,10)
                    buf_mas.append(a)
                else:
                    a = random.randint(-10,10)
                    buf_mas.append(a)
                    b = copy.deepcopy(buf_mas)
                    w_mas2.append(b)
                    buf_mas.clear()

    except NameError and ValueError:
        print("Ошибка ввода размерности")

if __name__ == '__main__':
    funk(l1, l2)#Example
    funk(lis1, lis2)

    enter()
    funk(w_mas1, w_mas2)