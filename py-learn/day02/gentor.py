# coding: utf-8


# 生成器的优点，用到什么地方，算到什么地方，懒计算机制
#
def feibo(n):
    a = 0
    b, count = 0, 1
    while a <= n:
        yield count
        b, count = count, count + b
        a = a + 1


if __name__ == '__main__':

    # 迭代器的第一种形式，（） 改写推导式
    a = (x ** 3 for x in range(11))
    # 注意的一点事生成器只能遍历一次
    for x in a:
        print x

    # 第二次遍历不生效，因为生成器没生效
    for y in a:
        print y

    # 第二种形式，定义成函数，使用时遍历， 生成器是迭代器的特殊形式
    hh = feibo(10)
    for fei in hh:
        print fei
