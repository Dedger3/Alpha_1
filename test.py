import copy

import numpy as np

ls1 = []
ls2 = []
result_array = []
count_list = []

def tesst():
    print("Введите размерность Первого массива через пробел:")
    count1, count2 = map(int, input().split())
    print("Введите размерность Второго массива через пробел:")
    count3, count4 = map(int, input().split())

    w_mas1 = []
    w_mas2 = []

    # Input funktions
    for i in range(count1): #2
        buf_mas = []
        for j in range(count2): #3
            if j != count2-1:
                a = (i) * count2 + (j+1)
                buf_mas.append(a)
            else:
                a = (i) * count2 + (j + 1)
                buf_mas.append(a)
                b = copy.deepcopy(buf_mas)
                w_mas1.append(b)
                buf_mas.clear()
    # Input funktions
    for i in range(count3): #2
        buf_mas = []
        for j in range(count4): #3
            if j != count4-1:
                a = (i)*count4 +(j+1)
                buf_mas.append(a)
            else:
                a = (i) * count4 + (j + 1)
                buf_mas.append(a)
                b = copy.deepcopy(buf_mas)
                w_mas2.append(b)
                buf_mas.clear()

    print(w_mas1)
    print(w_mas2)

    for i in range(len(w_mas1)):  # 2
        for j in range(len(w_mas2)):  # 3
            if j >= 1:
                continue
            for h in range(len(w_mas2[j])):  # 4
                sum_mas = 0
                for k in range(len(w_mas1[i])):  # 3
                    sum_mas += w_mas1[i][k]*w_mas2[k][h]
                    if k == len(w_mas1[i])-1:
                        count_list.append(sum_mas)
                        if h == len(w_mas2[j]) - 1:
                            b = copy.deepcopy(count_list)
                            result_array.append(b)
                            count_list.clear()
    fin = np.array(result_array)
    print(fin)