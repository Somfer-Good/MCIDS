from os import system
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

# Начальные настройки
h = 0
t = []
x = []
y = []
xe = []
ye = []


def Init(a, b):  # ИнициализацияЫ
    t.clear()
    x.clear()
    y.clear()
    xe.clear()
    ye.clear()

    D = Decisions(a)
    De = Euler(a, b)
    print(D)
    print(De)

    i = 0
    t.append(a)
    x.append(D[0])
    y.append(D[1])
    xe.append(De[0])
    ye.append(De[1])

    while i < b:
        i += h
        D = Decisions(i)
        De = Euler(xe[len(xe)-1], ye[len(ye)-1])

        t.append(i)
        x.append(D[0])
        y.append(D[1])
        xe.append(De[0])
        ye.append(De[1])


def f(x, y):  # f(x,y)
    return x-y


def g(x, y):  # g(x,y)
    return -4*x+y


def Decisions(t):  # x(t), y(t)
    return [5/4*pow(math.e, -t)+3/4*pow(math.e, 3*t), 5/2*pow(math.e, -t)-3/2*pow(math.e, 3*t)]


def Euler(x, y):  # Решения Эйлера
    return [x+f(x, y)*h, y+g(x, y)*h]


def Scaling():  # Графики
    plt.grid()
    ax.plot(x, y, c='b')
    ax.plot(xe, ye, c='r')
    plt.show()


def Table():  # Таблица
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    fig.patch.set_visible(False)
    ax.axis('tight')
    ax.axis('off')
    col_labels = ['T', 'X', 'Y', 'X_E', 'Y_E']
    table_vals = []
    for i in range(0, 50):
        tmp = [t[i], x[i], y[i], xe[i], ye[i]]
        table_vals.append(tmp)

    the_table = ax.table(cellText=table_vals,
                         colWidths=[0.3] * len(col_labels),
                         rowLoc='center',
                         colLabels=col_labels,
                         cellLoc="center",
                         loc='center')
    the_table.auto_set_font_size(True)
    the_table.set_fontsize(12)
    the_table.scale(1, 1)
    plt.show()


def Distance(x, y, x1, y1):  # Расстояние между двумя точками
    return math.sqrt(pow(x-x1, 2)+pow(y-y1, 2))


def MaxChange():  # Максимальное отклонение
    ans = Distance(x[0], y[0], xe[0], ye[0])
    for i in range(1, len(x)):
        ans = max(Distance(x[i], y[i], xe[i], ye[i]), ans)
    return ans


def menu():  # Меню выбора
    print('1. Меняем начальные настройки')
    print('2. Графики')
    print('3. Таблица')
    print('4. Максимальное расхождение')
    print('5. Выход')


exit = True
while (exit):
    print('Для продожений нажмите Enter')
    input()
    system("cls")
    menu()
    print('Выберете действие:', end='')
    select = int(input())
    if select == 1:
        print("Введите диапазон значений: ", end='')
        str = input()
        arr = str.split(' ')
        if len(arr) == 2:
            a = float(arr[0])
            b = float(arr[1])
        else:
            print('Неверное количество значений')
            continue
        print('Введите шаг:', end='')
        str = input()
        harr = str.split(' ')
        h = float(harr[0])
        Init(a, b)
        print('Настройки сохранены')
    elif select == 2:
        Scaling()
    elif select == 3:
        Table()
    elif select == 4:
        print(MaxChange())
    # elif select == 5:
       # Stability()
    elif select == 5:
        exit = False
    else:
        print("Некорректный пункт меню")
