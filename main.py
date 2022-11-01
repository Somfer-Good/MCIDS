from os import system
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

h=0
t = []
a = []
b = []
c = []

def Init(f,x,y):
    #print(type(f),type(x),type(y),type(h))
    a.clear()
    b.clear()
    c.clear()
    i=0
    t.append(x)
    while t[i]+h<y:
        t.append(round(t[i]+h,2))
        i += 1
    for i in range(0, len(t)):
        a.append(round(f / ((1 + f) * pow(math.e, -t[i]) - f),2))
        b.append(round(EulerB(a[i]),2))
        c.append(round(Rectangle(a[i]),2))


def Graph():
    plt.grid()
    ax.plot(t, a, c='b')
    ax.plot(t, b, c='r')
    ax.plot(t, c, c='g')
    plt.show()


def F(arg):
    return arg + pow(arg, 2)


def EulerB(arg):
    return arg + h * F(arg)


def Rectangle(arg):
    tmp = arg + h / 2 * F(arg)
    return arg + h * F(tmp)


def Scaling(scX1, scY1, scX2, scY2):
    plt.grid()
    ax.plot(t, a, c='b')
    ax.plot(t, b, c='r')
    ax.plot(t, c, c='g')
    plt.xlim(scX1, scX2)
    plt.ylim(scY1, scY2)
    plt.show()


def Table():
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    fig.patch.set_visible(False)
    ax.axis('tight')
    ax.axis('off')
    col_labels = ['T', 'A', 'B', 'C']
    table_vals = []
    for i in range(0, len(t)):
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


def MaxChange(Z, X, Y):
    Max1 = abs(Z[0] - X[0])
    Max2 = abs(Z[0] - Y[0])
    #print(t[0], end=' ')
    #print(Z[0], end=' ')
    #print(X[0], end=' ')
    #print(Y[0], end=' ')
    #print(Max1,end=' ')
    #print(Max2)
    for i in range(1, len(Z)):
        Max1 = max(Max1, abs(Z[i] - X[i]))
        Max2 = max(Max2, abs(Z[i] - Y[i]))
        #print(t[i], end=' ')
        #print(Z[i], end=' ')
        #print(X[i], end=' ')
        #print(Y[i], end=' ')
        #print(Max1, end=' ')
        #print(Max2)
    return [Max2, Max1]


def MaxSum(Z, X, Y):
    s1 = 0
    s2 = 0
    for i in range(0, len(Z)):
        s1 += (pow(Z[i] - X[i], 2))
        s2 += (pow(Z[i] - Y[i], 2))
    return [s2, s1]


def CheeckStability(r):
    if r < 0:
        return " Асимптотически устойчиво"
    elif r > 0:
       return " Не устойчиво"
    else:
        return " Нужна дополниельная проверка"


def Stability():
    x1 = -1
    x2 = 0
    print(x1, end=' ')
    print(x2, end=' ')
    print("Состояние рановесия")
    Fx1 = 1 + 2 * x1
    Fx2 = 1 + 2 * x2
    print(x1, end=' ')
    print(CheeckStability(Fx1))
    print(x2, end=' ')
    print(CheeckStability(Fx2))


def menu():
    print('1. Меняем начальные настройки')
    print('2. Графики')
    print('3. Таблица')
    print('4. Максимальное расхождение')
    print('5. Состояние равновесия')
    print('6. Выход')


exit = True
while (exit):
    print('Для продожений нажмите Enter')
    input()
    system("cls")
    menu()
    print('Выберете действие:', end='')
    select = int(input())
    if select == 1:
        print("Введите значение f=", end='')
        f = int(input())
        print("Введите диапазон значений: ", end='')
        str = input()
        arr = str.split(' ')
        if len(arr) == 2:
            x = float(arr[0])
            y = float(arr[1])
        else:
            print('Неверное количество значений')
            continue
        print('Введите шаг:', end='')
        str = input()
        harr = str.split(' ')
        h=float(harr[0])
        Init(f,x,y)
        print('Настройки сохранены')
    elif select == 2:
        Graph()
    elif select == 3:
        Table()
    elif select == 4:
        print(MaxChange(a, b, c))
        print(MaxSum(a, b, c))
    elif select == 5:
        Stability()
    elif select == 6:
        exit = False
    else:
        print("Некорректный пункт меню")