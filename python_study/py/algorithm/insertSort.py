#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 9:52
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : insertSort.py
# @Software: PyCharm

"""
直接插入排序算法：
思想：将一个新的数据插入到一个有序数组中，并继续保持有序，第后一个不断的与前一个比较
　　3,1,5,4,2
第一次排序，1比3小，则1和3换位置，变为了1,3,5,4,2
第二次排序，5比3大，不需要调整，仍未1,3,5,4,2
"""


def insertSort(data_list):
    finish_list = []
    finish_list.append(data_list[0])
    for num in range(1, len(data_list)):
        for pre in range(0, num):
            # 如果待加入的数据已经比已排好的最小数据还小，直接放在最前面就行
            if data_list[num] <= finish_list[pre]:
                finish_list.insert(pre, data_list[num])
                break
            # 如果待加入的数据已经比已排好最大值还大，直接放在最后面就行
            elif data_list[num] >= finish_list[-1]:
                finish_list.append(data_list[num])
                break
            elif data_list[num] >= finish_list[pre] and data_list[num] < finish_list[pre + 1]:
                finish_list.insert(pre + 1, data_list[num])
                break
            else:
                pass
    return finish_list


"""
选择排序:
是每一次从待排序的数据元素中选出最小的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完
"""


def chooseSort(data_list):
    N = len(data_list)
    for num in range(N):
        for pre in range(num + 1, N):
            if data_list[num] <= data_list[pre]:
                pass
            else:
                data_list[num], data_list[pre] = data_list[pre], data_list[num]
    return data_list


def chooseSortNew(data_list):
    N = len(data_list)
    num = 0
    while num < N:
        for index in range(num, N):
            if data_list[num] <= data_list[index]:
                pass
            else:
                data_list[num], data_list[index] = data_list[index], data_list[num]
        num += 1
    return data_list


"""
冒泡算法的运作规律如下：
　　①、比较相邻的元素。如果第一个比第二个大，就交换他们两个。
　　②、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数（也就是第一波冒泡完成）。
　　③、针对所有的元素重复以上的步骤，除了最后一个。
　　④、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubblSort(data_list):
    N = len(data_list)
    for num in range(N):
        for index in range(num, N - 1):
            if data_list[index] > data_list[index + 1]:
                data_list[index + 1], index[index] = data_list[index], data_list[index + 1]
    return data_list


def bubblSortNew(data_list):
    N = len(data_list)
    index = N - 1
    while index > 0:
        num = 0
        while num < index:
            if data_list[num] > data_list[num + 1]:
                data_list[num], data_list[num + 1] = data_list[num + 1], data_list[num]
        index -= 1
    return data_list


if __name__ == "__main__":
    data_list = [5, 1, 7, 9, 3, 3, 4, 6]

    print("源数据：" + str(data_list))
    print(insertSort(data_list))
    print(chooseSort(data_list))
    print(chooseSortNew(data_list))
    print(bubblSort(data_list))
    print(bubblSortNew(data_list))
