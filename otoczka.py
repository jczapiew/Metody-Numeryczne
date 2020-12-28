import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(num_list1, num_list2, num_list3):
    swapped = True
    while swapped:
        swapped = False
        for ints in range(len(num_list1) - 1):
            if num_list1[ints] > num_list1[ints+1]:
                num_list1[ints], num_list1[ints+1] = num_list1[ints+1], num_list1[ints]
                num_list2[ints], num_list2[ints+1] = num_list2[ints+1], num_list2[ints]
                num_list3[ints], num_list3[ints+1] = num_list3[ints+1], num_list3[ints]
                swapped = True

def wyznacznik(x1,x2,x3,y1,y2,y3):
    return x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1*y3

def strona(wierzcholki, x, y, i3):
    i2 = wierzcholki[-1]
    i1 = wierzcholki[-2]
    if wyznacznik(x[i1],x[i2],x[i3],y[i1],y[i2],y[i3])>=0:
        return 0
    if wyznacznik(x[i1],x[i2],x[i3],y[i1],y[i2],y[i3])<0:
        return 1

def pentagram(x,y,h,x_penta,y_penta):
    x1 = x
    y1 = y + h
    x2 = x + h * np.cos(0.6 * np.pi)
    y2 = y - h * np.cos(0.6 * np.pi)
    x3 = x + h * np.cos(0.6 * np.pi)
    y3 = y + h * np.cos(0.8 * np.pi)
    x4 = x - h * np.cos(0.6 * np.pi)
    y4 = y + h * np.cos(0.8 * np.pi)
    x5 = x - h * np.cos(0.6 * np.pi)
    y5 = y - h * np.cos(0.6 * np.pi)

    x_penta.append(x1)
    x_penta.append(x2)
    x_penta.append(x3)
    x_penta.append(x4)
    x_penta.append(x5)
    y_penta.append(y1)
    y_penta.append(y2)
    y_penta.append(y3)
    y_penta.append(y4)
    y_penta.append(y5)

    plt.plot((x3,x1),(y3,y1), color='black')
    plt.plot((x1,x4),(y1,y4), color='black')
    plt.plot((x3,x5),(y3,y5), color='black')
    plt.plot((x2,x4),(y2,y4), color='black')
    plt.plot((x2,x5),(y2,y5), color='black')

def grahamix(x,y,alfa):
    miny = 100
    minx = 100
    yindex = []
    xindex = 0
    for whys in range(len(y)):
        if y[whys] <= miny:
            miny = y[whys]
            yindex.append(whys)
    iterat = -1
    for indexes in range(len(yindex)):
        if y[yindex[iterat]] != miny: break
        if x[yindex[iterat]] < minx:
            xindex = yindex[iterat]
            minx = x[yindex[iterat]]
        iterat = iterat - 1

    for deeds in range(len(x)):
        if deeds == xindex:
            alfa.append(0)
            continue
        if x[deeds] < x[xindex]:
            alfa.append(2 - ((y[deeds] - y[xindex]) / (y[deeds] - y[xindex] + abs(x[deeds] - x[xindex]))))
        else:
            alfa.append((y[deeds] - y[xindex]) / (y[deeds] - y[xindex] + abs(x[deeds] - x[xindex])))

def wierzcholkowo(otoczka,x,y):
    aniteration = 3
    while aniteration < len(x):
        while strona(otoczka, x, y, aniteration) == 1:
            otoczka.pop()
        otoczka.append(aniteration)
        aniteration += 1
    otoczka.append(0)

h = 15
x = []
y = []
keep_going = False
iteration = 0
while iteration<20:
    into_x = np.random.randint(100)
    into_y = np.random.randint(100)

    if iteration != 0:
        for ints in range(iteration):
            if x[ints] == into_x and y[ints] == into_y: keep_going = True
    if keep_going:
        keep_going = False
        continue

    x.append(into_x)
    y.append(into_y)
    iteration += 1

alpha = []

grahamix(x,y,alpha)
bubble_sort(alpha,x,y)

otoczka = []
otoczka.append(0)
otoczka.append(1)
otoczka.append(2)

wierzcholkowo(otoczka,x,y)

for ints in range(len(x)):
    plt.plot(x,y, 'ok', color='blue')

x1 = []
y1 = []
for ints in range(len(otoczka)):
    x1.append(x[otoczka[ints]])
    y1.append(y[otoczka[ints]])
for ints in range(len(x1)-1):
    plt.plot((x1[ints],x1[ints+1]),(y1[ints],y1[ints+1]), color='red')
x666=x
y666=y
for ints in range(len(x)):
    pentagram(x[ints],y[ints],h,x666,y666)

alpha2 = []
grahamix(x666,y666,alpha2)
bubble_sort(alpha2,x666,y666)
otoczka2 =[]
otoczka2.append(0)
otoczka2.append(1)
otoczka2.append(2)
wierzcholkowo(otoczka2,x666,y666)
x6661 = []
y6661 = []
for ints in range(len(otoczka2)):
    x6661.append(x666[otoczka2[ints]])
    y6661.append(y666[otoczka2[ints]])
for ints in range(len(x6661)-1):
    plt.plot((x6661[ints],x6661[ints+1]),(y6661[ints],y6661[ints+1]), color='red')

plt.show()