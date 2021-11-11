import numpy as np
def funk():
    lst1 = []
    lst2 = []
    lenth = 0
    n = 0
    #Enter 2-dimentional arrays

    while True:
        #print("Нажмите 1, чтобы ввести матрицы вручную, 2- чтобы ввести только размерность матрицы, 3- чтобы всё произошло автоматиче")
        print("Нажмите 1, чтобы ввести матрицы вручную")
        a = input()
        if a == "1":
            while True:
                if n == 0:
                    try:
                        lst = list(map(float, input().split(" ")))
                        lenth = len(lst)
                        lst1.append(lst)
                        n = 1
                        continue
                    except:
                        break

                if n == 1:
                    try:
                        lst = list(map(float, input().split(" ")))
                        if len(lst) != lenth:
                            a = []
                            print(f"Ошибка ввода: {a}")
                            n = 0
                            lenth = 0
                            break
                    except:
                        n = 0
                        lenth = 0
                        break
                lst1.append(lst)

            while True:
                if n == 0:
                    try:
                        lst = list(map(float, input().split(" ")))
                        lenth = len(lst)
                        lst2.append(lst)
                        n = 1
                        continue
                    except:
                        break

                if n == 1:
                    try:
                        lst = list(map(float, input().split(" ")))
                        if len(lst) != lenth:
                            a = []
                            print(f"Ошибка ввода: {a}")
                            break
                    except:
                        break
                lst2.append(lst)

            break
#2
        '''elif a == "2":
            i = 0
            print("Введите размеры первой матрицы через пробел:")
            try:
                num1, num2 = map(int, input().split())
                num3, num4 = map(int, input().split())
                if num2 == num3:
                    try:
                        lst1 = list(range(1,num1 + num2))
                        lst2 = list(range(1,num3 + num4))
                        print(lst1)
                        print(lst2)
                        break
                    except:
                        continue
            except(ValueError):
                print("Вы ввели неверное значение")
                continue
            if i == 1:
                break
        elif a == 3:

            break
        else:
            print("Введите корректное число")'''

    #change from List[list] to arrays
    ar1 = np.array(lst1)
    b = np.transpose(ar1)
    ar1_strings = np.vsplit(ar1, len(b[0]))

    ar2 = np.array(lst2)
    c = ar2
    ar2 = np.transpose(ar2)
    ar2_strings = np.vsplit(ar2, len(c[0]))


    if len(ar1[0]) != len(ar2[0]):
        print("Неверный размер")

    result_array = []
    for i in range(len(ar1_strings)):
        for j in range(len(ar2_strings)):
            for k in range(len(ar1_strings[j])):
                #print(ar1_strings[i][k]*ar2_strings[j][k])

                result_array.append(sum(ar1_strings[i][k]*ar2_strings[j][k]))
    #(len(ar1[0]), len(c[0]))

    a = np.array(result_array).reshape(len(ar1),len(c[0]))
    print(a)


if __name__ == '__main__':
    funk()