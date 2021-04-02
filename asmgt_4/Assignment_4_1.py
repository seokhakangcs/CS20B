from matplotlib import pyplot as plt


def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]


readSet1 = open("/Users/kang/Documents/CS20B/asmgt_4/rainfallISet1.txt", "r")
readSet2 = open("/Users/kang/Documents/CS20B/asmgt_4/rainfallSet2.txt", "r")
data1 = []
data2 = []
data_name_1 = []
data_value_1 = []
data_name_2 = []
data_value_2 = []

while True:
    line = readSet1.readline()
    if not line:
        break
    data1 = line.split()
    data_name_1.append(data1[0])
    data_value_1.append(float(data1[1]))

while True:
    line2 = readSet2.readline()
    if not line2:
        break
    data2 = line2.split()
    data_name_2.append(data2[0])
    data_value_2.append(float(data2[1]))

value_a_x = create_x(3, 0.8, 1, 25)
value_b_x = create_x(3, 0.8, 2, 25)

ax = plt.subplot()
ax.bar(value_a_x, data_value_1)
ax.bar(value_b_x, data_value_2)
middle_x = [(a+b)/2 for (a, b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(data_name_1, rotation=90)

plt.show()
