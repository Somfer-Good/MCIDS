from os import system
import matplotlib.pyplot as plt
import math

# Начальные настройки
h = 0
t = []
x = []
y = []
xe = []
ye = []


def Init(p, p1):  # Инициализация
    a = 2
    b = 1
    t.clear()
    x.clear()
    y.clear()
    xe.clear()
    ye.clear()

    D = Decisions(p)
    De = Euler(a, b)
    #print(D)
    #print(De)

    i = 0
    t.append(p)
    x.append(D[0])
    y.append(D[1])
    xe.append(De[0])
    ye.append(De[1])

    while i < p1:
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
    fig.set_figwidth(8)
    fig.set_figheight(8)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    ax.scatter(x, y, c='red', label="В явном виде",s=1)  # Красный в явном виде
    ax.scatter(xe, ye, c='blue', label="Метод Эйлера",s=0.5)  # Синий Эйлер
    plt.legend(fontsize=14)
    plt.tight_layout()
    plt.show()


def Table():  # Таблица
    fig.set_figwidth(10)
    fig.set_figheight(10)
    fig.patch.set_visible(False)
    ax.axis('tight')
    ax.axis('off')
    col_labels = ['T', 'X', 'Y', 'X_E', 'Y_E']
    table_vals = []
    size=0
    if len(x)>50: size=51
    else: size=len(x)
    for i in range(0, size):
        tmp = [t[i], x[i], y[i], xe[i], ye[i]]
        table_vals.append(tmp)

    the_table = ax.table(cellText=table_vals,
                         colWidths=[0.2] * len(col_labels),
                         rowLoc='center',
                         colLabels=col_labels,
                         cellLoc="center",
                         loc='center')
    the_table.auto_set_font_size(True)
    the_table.set_fontsize(12)
    the_table.scale(1, 1)
    plt.show()

def СheckSpecialpoint(l1,l2,b1=0,b2=0):
    print('Особая точка (0;0) - ', end='')
    if l1<0 and l2<0 and b1==0 and b2==0: print('Устойчивый узел')
    elif l1>0 and l2>0 and b1==0 and b2==0: print('Неустойчивый узел')
    elif l1>0 and l2<0 and b1==0 and b2==0 or l1<0 and l2>0 and b1==0 and b2==0: print('Седло')
    elif l1<0 and l2<0 and b1!=0 and b2!=0: print('Устойчивый фокус')
    elif l1>0 and l2>0 and b1!=0 and b2!=0: print('Неустойчивый фокус')
    else: print('Неизвестно')



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
    print('3. Таблица значений(первые 50)')
    print('4. Вид особой точки')
    print('5. Максимальное расхождение')
    print('6. Выход')


exit = True
while (exit):
    fig, ax = plt.subplots()
    print('Для продожений нажмите Enter')
    input()
    h=0.001
    Init(0,2)
    system("cls")
    menu()
    print('Выберете действие: ', end='')
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
        print('Введите шаг: ', end='')
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
       СheckSpecialpoint(-1,3)
    elif select == 5:
        print(MaxChange())
    elif select == 6:
        exit = False
    else:
        print("Некорректный пункт меню")
