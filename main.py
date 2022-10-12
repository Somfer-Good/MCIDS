from os import system
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

h = 0.01
t = []
a = []
b = []
c = []


def Graph():
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.grid()
    ax.plot(t, a, c='b')
    ax.plot(t, b, c='r')
    ax.plot(t, c, c='g')
    plt.show()


def F(arg):
    return arg + pow(arg, 2)


def DefaultDecisionA(arg):
    return 1 / (3 / 2 * (pow(math.e, arg)) - 1) - 1


def EulerB(arg):
    return arg + h * F(arg)


def Rectangle(arg):
    tmp = arg + h / 2 * F(arg)
    return arg + h * F(tmp)


def Preparation():
    i = 0
    t.append(0)
    a.append(DefaultDecisionA(t[i]))
    b.append(EulerB(a[i]))
    c.append(Rectangle(a[i]))
    while t[i] < 1:
        i += 1
        t.append(round(t[i - 1] + h, 2))
        a.append(DefaultDecisionA(t[i]))
        b.append(EulerB(a[i]))
        c.append(Rectangle(a[i]))


def Scaling(scX1, scY1, scX2, scY2):
    plt.grid()
    ax.plot(t, a, c='b')
    ax.plot(t, b, c='r')
    ax.plot(t, c, c='g')
    plt.xlim(scX1, scX2)
    plt.ylim(scY1, scY2)
    plt.show()


def Table(i):
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    fig.patch.set_visible(False)
    ax.axis('tight')
    ax.axis('off')
    col_labels = ['T', 'A', 'B', 'C']
    table_vals = []
    if i == 0:
        s = 55
        o = 0
    else:
        o = 55
        s = len(t)
    for i in range(o, s):
        tmp = [t[i], a[i], b[i], c[i]]
        table_vals.append(tmp)

    the_table = ax.table(cellText=table_vals,
                         colWidths=[0.3] * 4,
                         rowLoc='center',
                         colLabels=col_labels,
                         cellLoc="center",
                         loc='center')
    the_table.auto_set_font_size(True)
    the_table.set_fontsize(12)
    the_table.scale(1, 1)
    plt.show()


def menu():
    print('1. Графики')
    print('2. Таблица')
    print('3. Просмотр таблицы (далее)')
    print('4. Просмотр таблицы (назад)')
    print('5. Изменения масштаба(график)')
    print('6. Выход')


Preparation()
ts = 0
gr = False
tb = False
exit = True
while (exit):
    print('Для продожений нажмите Enter')
    input()
    system('clear')
    menu()
    print('Выберете действие:', end='')
    select = int(input())
    if select == 1:
        Graph()
        gr = True
        tb = False
    elif select == 2:
        Table(ts)
        gr = False
        tb = True
    elif select == 3:
        if not tb:
            print('Для продлжения выберите пункт 2')
            continue
        ts += 1
        if (ts > 4):
            ts = 0
        Table(ts)
    elif select == 4:
        if not tb:
            print('Для продлжения выберите пункт 2')
            continue
        ts -= 1
        if (ts < 0):
            ts = 1
        Table(ts)
    elif select == 5:
        if not gr:
            print('Для продлжения выберите пункт 1')
            continue
        print('Введите область по X: ', end='')
        strx = input()
        arrX = strx.split(' ')
        if len(arrX) == 2:
            x1 = float(arrX[0])
            x2 = float(arrX[1])
        else:
            print('Неверное количество значений')
            continue
        print('Введите область по Y: ', end='')
        stry = input()
        arrY = stry.split(' ')
        if len(arrY) == 2:
            y1 = float(arrY[0])
            y2 = float(arrY[1])
        else:
            print('Неверное количество значений')
            continue
        Scaling(x1, y1, x2, y2)
    elif select == 6:
        exit = False
    else:
        print("Некорректный пункт меню")
