"""

定义和使用列表
	- 用下标访问元素
	- 添加元素
	- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06

"""


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)  # ['grape', '@pple', 'strawberry', 'waxberry']
    # 通过下标访问元素
    print(fruits[0])  # grape
    print(fruits[1])  # @pple
    print(fruits[-1])  # waxberry
    print(fruits[-2])  # strawberry
    # print(fruits[-5]) # IndexError
    # print(fruits[4])	# IndexError
    fruits[1] = 'apple'
    print(fruits)  # ['grape', 'apple', 'strawberry', 'waxberry']
    # 添加元素
    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)  # ['banana', 'grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 删除元素
    del fruits[1]  #删除index=1的元素
    print(fruits)  # ['banana', 'apple', 'strawberry', 'waxberry', 'pitaya']
    fruits.pop()  #删除最后一个元素
    print(fruits)  # ['banana', 'apple', 'strawberry', 'waxberry']
    fruits.pop(0)  #删除index=0的元素
    print(fruits)  # ['apple', 'strawberry', 'waxberry']
    fruits.remove('apple')
    print(fruits)  # ['strawberry', 'waxberry']


if __name__ == '__main__':
    main()
