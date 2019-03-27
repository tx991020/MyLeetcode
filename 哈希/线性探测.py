

import random

INDEXBOX = 10
MAXNUM = 7


def create_table(num, index):
    tmp = num % INDEXBOX
    while True:
        if index[tmp] == -1:
            index[tmp] = num
            break
        else:
            tmp = (tmp + 1) % INDEXBOX


# 主程序


def print_data(data, max_number):
    for i in range(max_number):
        print(data[i])


index = [None]*INDEXBOX
data = [None]*MAXNUM

if __name__ == '__main__':
    print("原始数组值：")

    for i in range(MAXNUM):
        data[i] = random.randint(1, 20)  # 起始数据值
    for i in range(INDEXBOX):
        index[i] = -1

    print_data(data, MAXNUM)  # 打印启始数据

    print("哈希表内容：")

    for i in range(MAXNUM):
        create_table(data[i], index)
        print_data(index, INDEXBOX)

    print("完成哈希表")
    print_data(index, INDEXBOX)  # 打印最后完成的结果







