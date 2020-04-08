# coding: utf-8

class Singleton(type):

    # 初始化 类对象，给类对象附一个属性值
    def __init__(self, *args, **know):
        self._instance = None
        super(Singleton, self).__init__(*args, **know)

    # 将类对象创建的实例对象 赋值给自身的 instance 属性
    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class Test(object):
    __metaclass__ = Singleton


if __name__ == '__main__':
    a = Test()
    b = Test()

    print (a == b)
