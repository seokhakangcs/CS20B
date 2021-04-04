from matplotlib import pyplot as plt


readSet1 = open("/Users/kang/Documents/CS20B/asmgt_4/rainfallISet1.txt", "r")
readSet2 = open("/Users/kang/Documents/CS20B/asmgt_4/rainfallSet2.txt", "r")
data1 = []
data2 = []
dict1 = {}
dict2 = {}
data_name_1 = []
data_value_1 = []
data_name_2 = []
data_value_2 = []
while True:
    line = readSet1.readline()
    if not line:
        break
    # print(line)
    data1 = line.split()
    dict1[data1[0]] = data1[1]
    data_name_1.append(data1[0])
    data_value_1.append(float(data1[1]))
    print(data1)
# print("data1\n")
print('\n')

while True:
    line2 = readSet2.readline()
    if not line2:
        break
    # print(line)
    data2 = line2.split()
    dict2[data2[0]] = data2[1]
    data_name_2.append(data2[0])
    data_value_2.append(float(data2[1]))
    print(data2)
# print("data2\n")

print(len(dict1))
print(len(dict2))
print(data_name_1)
print(data_value_1)
print('\n')
print(data_name_2)
print(data_value_2)

topics = ['A', 'B', 'C', 'D', 'E']
value_a = [80, 85, 84, 83, 86]
value_b = [73, 78, 77, 82, 86]
value_c = [x*2 for x in range(25)]
value_d = [x*2 + 50 for x in range(25)]
print(value_c)
print(value_d)


def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]


# value_a_x = create_x(3, 0.8, 1, 25)
# value_b_x = create_x(3, 0.8, 2, 25)

# ax = plt.subplot()
# ax.bar(value_a_x, data_value_1)
# ax.bar(value_b_x, data_value_2)
# middle_x = [(a+b)/2 for (a, b) in zip(value_a_x, value_b_x)]
# ax.set_xticks(middle_x)
# ax.set_xticklabels(data_name_1, rotation=90)

colors = ['y'] * 25
bx = plt.subplot()
bx.bar(value_c, data_value_1, color=colors)
bx.bar(value_d, data_value_2, color=colors)
bx.set_xticks(value_c + value_d)
bx.set_xticklabels(data_name_1 + data_name_2, rotation=90)

# bx.plot(kind='bar', colors=colors)
plt.show()
