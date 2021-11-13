import copy

ls1 = []
ls2 = []
result_array = []

def tesst():
    print("Введите размерность Первого массива через пробел:")
    count1, count2 = map(int, input().split())
    print("Введите размерность Второго массива через пробел:")
    count3, count4 = map(int, input().split())
    w_mas1 = []
    w_mas2 = []

    for i in range(count1): #2
        buf_mas = []
        for j in range(count2): #3
            if j != count2-1:
                a = (i+1)*(j+1)
                buf_mas.append(a)
            else:
                a = (i + 1) * (j + 1)
                buf_mas.append(a)
                b = copy.deepcopy(buf_mas)
                w_mas1.append(b)
                buf_mas.clear()

    for i in range(count3): #2
        buf_mas = []
        for j in range(count4): #3
            if j != count4-1:
                a = (i+1)*(j+1)
                buf_mas.append(a)
            else:
                a = (i + 1) * (j + 1)
                buf_mas.append(a)
                b = copy.deepcopy(buf_mas)
                w_mas2.append(b)
                buf_mas.clear()

    print(w_mas1)
    print(w_mas2)

    '''for i in range(len(ls1)):  # 6
        for j in range(len(ls2)):  # 12
            for k in range(len(ls1[j])):  # 2
                result_array.append(ls1[i][k] * ls2[j])'''

