def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)            #[1, 3, 5, 7, 100]
    list2 = ['hello'] * 5
    print(list2)            #['hello', 'hello', 'hello', 'hello', 'hello']

    # 计算列表长度(元素个数)
    print(len(list1))       #5,list元素的个数

    # 下标(索引)运算
    print(list1[0])         #1
    print(list1[4])         #100
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])         #100,用-1做索引，直接获取最后一个元素
    print(list1[-3])         #5

    list1[2] = 300
    print(list1)            #[1, 3, 300, 7, 100]

    # 添加元素
    list1.append(200)       #往list中追加元素到末尾
    print(list1)            #[1, 3, 300, 7, 100, 200]
    list1.insert(1, 400)    #把元素插入到指定的位置，比如索引号为1的位置
    print(list1)            #[1, 400, 3, 300, 7, 100, 200]
    list1 += [1000, 2000]   #
    print(list1)            #[1, 400, 3, 300, 7, 100, 200, 1000, 2000]
    print(len(list1))       #9

    # 删除元素
    list1.remove(300)       #删除元素300
    print(list1)            #[1, 400, 3, 7, 100, 200, 1000, 2000]
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]            #删除index=0的元素
    print(list1)            #[400, 3, 7, 100, 200, 1000, 2000]
    # 清空列表元素
    list1.clear()
    print(list1)            #[]

if __name__ == '__main__':
    main()
