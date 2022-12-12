#================================================Область объявления функций======================================================
# функция для вывода многочлена
def output_polynomial(List_coef):
    ans = ''
    for i in range(len(List_coef)):
        if (List_coef[i] != 0): # есть ли смысл выводить
            # вывод знака +
            if (i != 0 and List_coef[i] > 0):
                ans += "+"
            # вывод х и множителя перед ним
            if (i != len(List_coef) - 1):
                if (List_coef[i] == 1):
                    ans += "x"
                elif (List_coef[i] == -1):
                    ans += "-x"
                else:
                    ans += f"{List_coef[i]}x"
                # вывод степени х
                if (i != len(List_coef) - 2):
                    ans += f"^{len(List_coef) - 1 - i}"
            else:
                ans += str(List_coef[i])
    print(ans)

# функция для нахождения производной многочлена
def derivative(List_coef):
    new_polynomial = [0 for _ in range(len(List_coef) - 1)] # для храниения нового многочлена
    for j in range(len(List_coef) - 1):
        new_polynomial[j] = List_coef[j] * (len(List_coef) - 1 - j)
    output_polynomial(new_polynomial)

# деление столбиком многочленов
def division_polinomials(List_coef1, List_coef2):
    k = abs(List_coef1[0] / List_coef2[0])
    q = (len(List_coef1) - 1) - (len(List_coef2) - 1)

    # заталкиваем 0 в конец многочлена (делителя) чтобы не вылезать за диапазон
    for j in range(len(List_coef1) - len(List_coef2)):
        List_coef2.append(0)
    # определяем знак что мы будем делать + или -
    if (List_coef2[0] >= 0 and List_coef1[0] >= 0):
        flag_sign = False
    else:
        flag_sign = True
    for i in range(len(List_coef1)):
        if (flag_sign == False):
            List_coef1[i] = List_coef1[i] - List_coef2[i] * k
        else:
            List_coef1[i] = List_coef1[i] + List_coef2[i] * k

    List_coef1 = List_coef1[1:]
    output_polynomial(List_coef1)

#================================================Область объявления функций======================================================

# основное задание
#==================================Ввод и проверки входных данных============================
degree = input("Введите степень многочлена:\n")
# проверка корректности ввода степени
try:
    degree = int(degree)
except:
    print("Неверный тип данных -> ERROR")
    exit()
if (degree <= 0):
    print("Степень многочлена должна быть больше 0 -> ERROR")
    exit()

coef = input("Введите коэффиценты в порядке убывания степеней:\n").split()
# проверка корректности ввода коэффицентов
try:
    coef = list(map(int, coef))
except:
    print("Неверный тип данных -> ERROR")
    exit()
# проверка парвильного количества введённых коэффицентов
if (len(coef) > degree + 1 or len(coef) < degree + 1):
    print("Вы ввели недостаточное или избыточное кол-во коэффицентов -> ERROR")
    exit()

print("Вы ввели многочлен:")
output_polynomial(coef)

# Ввод точности аппроксимации
approx = input("Введите параметр точности аппроксимации:\n")
try:
    approx = int(approx)
except:
    print("Должно быть введено число -> ERROR")
    exit()
if (approx <= 0):
    print("Должно быть введено натуральное число -> ERROR")
    exit()

L1 = [-8, 4]
L2 = [1, 1]
division_polinomials(L1, L2)