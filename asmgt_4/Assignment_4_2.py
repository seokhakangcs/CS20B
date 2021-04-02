from matplotlib import pyplot as plt


def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]


def getMaxIndexFromList(datas):
    max_index = 0
    for i in range(len(datas)):
        if datas[i] > datas[max_index]:
            max_index = i
    return max_index


def getMinIndexFromList(datas):
    min_index = 0
    for i in range(len(datas)):
        if datas[i] < datas[min_index]:
            min_index = i
    return min_index


readSet1 = open("/Users/kang/Documents/CS20B/asmgt_4/rainfallISet1.txt", "r")
readSet2 = open("/Users/kang/Documents/CS20B/asmgt_4/rainfallSet2.txt", "r")
data1 = []
data2 = []
data_name_1 = []
data_value_1 = []
data_name_2 = []
data_value_2 = []
value_c = [x*3 for x in range(25)]
value_d = [x*3 + 75 for x in range(25)]


while True:
    line = readSet1.readline()
    if not line:
        break
    data1 = line.split()
    data_name_1.append(data1[0]+"(1)")
    data_value_1.append(float(data1[1]))

while True:
    line2 = readSet2.readline()
    if not line2:
        break
    data2 = line2.split()
    data_name_2.append(data2[0]+"(2)")
    data_value_2.append(float(data2[1]))

max_data_1 = data_value_2[0]


value_a_x = create_x(3, 0.8, 1, 25)
value_b_x = create_x(3, 0.8, 2, 25)

print(getMaxIndexFromList(data_value_2))

colors_1 = ['y'] * 25
colors_2 = ['y'] * 25
colors_1[getMaxIndexFromList(data_value_1)] = 'b'
colors_1[getMinIndexFromList(data_value_1)] = 'r'
colors_2[getMaxIndexFromList(data_value_2)] = 'b'
colors_2[getMinIndexFromList(data_value_2)] = 'r'
bx = plt.subplot()
bx.bar(value_c, data_value_1, color=colors_1)
bx.bar(value_d, data_value_2, color=colors_2)
bx.set_xticks(value_c + value_d)
bx.set_xticklabels(data_name_1 + data_name_2, rotation=90)

plt.show()
