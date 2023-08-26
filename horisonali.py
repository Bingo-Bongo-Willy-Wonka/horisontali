import numpy as np

file = open(r"C:\Users\Aydar\Desktop\horisontali.dat", "r")
data = file.readlines()
file.close()
print(data)

x = []
y = []
h = []
for i in range(0,len(data)):
    x.append("")
    y.append("")
    h.append("")
    x[i] = data[i].split(" ")[1]
    y[i] = data[i].split(" ")[2]
    h[i] = data[i].split(" ")[4]
for i in range(0, len(h)):
    h[i] = h[i].replace("\n", "")

for i in range(0, len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])
    h[i] = float(h[i])

print("")
print("x:", x)
print("y:", y)
print("h:", h)
print("округленное h:", int(float(h[1])))
print(len(x), len(y), len(h))
#если в списке х есть точка  такая что она больше Х-10 и меньше Х+10 то смотрим разность высот
#если высота найденной точки больше чем округленная до меньшего значения высота точки (Х, У) то строим линию
# и находим точку горизантали            j опорная, i найденнная в радиусе 15 точки j

linii = []
gotovo = []
for j in range(0, len(x)):
    for i in range(0, len(x)):
        if x[i] < x[j]+15 and x[i] > x[j] - 15:
            if y[i] < y[j]+15 and y[i] > y[j] - 15:
                #проверка на высоту:
                h_i = int(float(h[i]))
                h_j = int(float(h[j]))
                if h_i > h_j and abs(h_j-h_i) == 1:
                    # строим линию и находим точку на горизонтали
                    # linii.append([x[j], y[j]]) промежуточная проверка...
                    dx = x[i] - x[j]
                    dy = y[i] - y[j]
                    a = np.arctan(abs(dy/dx))
                    #print(a)
                    l = abs((h_i-h[j])/(h[i]-h[j]))*((dx**2+dy**2)**0.5)
                    #print(l)
                    if dx > 0:
                        if dy > 0:
                            x_got = x[j] + l*np.cos(a)
                            y_got = y[j] + l*np.sin(a)
                        if dy < 0:
                            x_got = x[j] + l * np.cos(a)
                            y_got = y[j] - l * np.sin(a)
                    if dx < 0:
                        if dy > 0:
                            x_got = x[j] - l*np.cos(a)
                            y_got = y[j] + l*np.sin(a)
                        if dy < 0:
                            x_got = x[j] - l * np.cos(a)
                            y_got = y[j] - l * np.sin(a)
                    x_got = round(x_got, ndigits=3)
                    y_got = round(y_got, ndigits=3)
                    gotovo.append([x_got, y_got])
print("gotovo:", gotovo)
done = open(r"C:\Users\Aydar\Desktop\gotovo.dat", "w")
for i in range(0, len(gotovo)):
    gotovo[i][0] = str(gotovo[i][0])
    gotovo[i][1] = str(gotovo[i][1])
    done.write(gotovo[i][0])
    done.write("    ")
    done.write(gotovo[i][1])
    done.write("\n")

# ...промежуточная проверка
# print(linii)
# tochki = open(r"C:\Users\Aydar\Desktop\tochki.dat", "w")
# print(linii[0][0])
# for i in range(0, len(linii)):
#     linii[i][0] = str(linii[i][0])
#     linii[i][1] = str(linii[i][1])
#     tochki.write(linii[i][0])
#     tochki.write("    ")
#     tochki.write(linii[i][1])
#     tochki.write("\n")

