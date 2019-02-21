#选择排序
def xuanzepaixu(list):
    for i in range(len(list)-1):
        for j in range(1,len(list)-i):
            if list[i]>list[i+j]:
                list[i],list[i+j] = list[i+j],list[i]
    return (list)

#冒泡排序
def maopaopaixu(list):
    for x in range(len(list)-1):
        for y in range(len(list)-x-1):
            if list[y]<list[y+1]:
                list[y],list[y+1] = list[y+1],list[y]
    return (list)

#快速排序
def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        # 由所有小于基准值的元素组成的子数组
        less = [m for m in array[1:] if m < baseValue]
        # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
        equal = [w for w in array if w == baseValue]
        # 由所有大于基准值的元素组成的子数组
        greater = [n for n in array[1:] if n > baseValue]
    return quickSort(less) + equal + quickSort(greater)

num = [55,23,69,2,30,14,102,204,10,28,15874,11,30]
print(maopaopaixu(num))

num1 = sorted(num)
print(num1)

#斐波那数列
n =int(input())
list1 = []
for t in range(n):
    if t==1 or t==0:
        list1.append(1)
    if t>1:
        list1.append(list1[t-1]+list1[t-2])

print(list1[n-1])

#二分查找法
def bin_search(data_list, val):
    low = 0                         # 最小数下标
    high = len(data_list) - 1       # 最大数下标
    while low <= high:
        mid = (low + high) // 2     # 中间数下标
        if data_list[mid] == val:   # 如果中间数下标等于val, 返回
            return mid+1
        elif data_list[mid] > val:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:                       # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return # val不存在, 返回None


list2 = [1,2,5,9,23,45,69,188,210]
print(bin_search(list2,5))