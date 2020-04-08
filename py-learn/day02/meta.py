# coding: utf-8


class SingletonMetaClass(type):
    # SingletonMetaClass 是元类，SingletonMetaClass() 返回的是一个 TestCls 类对象， init是初始化 TestCls 这个类对象，
    # TestCls 类对象里面有个_instance属性
    def __init__(cls, *args, **kwargs):
        print "ppp"
        cls._instance = None
        super(SingletonMetaClass, cls).__init__(*args, **kwargs)

    # call 方法首先检查 TestCls类对象 的属性是否为none, 对 类对象 TestCls 的属性赋值
    # TestCls 类对象创建 实例对象时，会显示的调用这个方法，此时创建的 _instance 是实例对象而不是类对象。
    # 总结：元类中的 call 方法创建的是 子类的 实例对象
    def __call__(cls, *args, **kwargs):
        """call 这里的执行 call方法 是类对象， 从而创建实例对象 """
        """
        如果元类中定义了__call__，此方法必须返回一个对象，否则类的实例化就不会起作用。（实例化得到的结果为__call__的返回值）
        如果元类的__call__中返回type.__call__(cls, *args, **kwargs),type创建的对象,里面会调用Foo的__new__方法,和__init__方法
        """
        print "oooooooo"
        if not cls._instance:
            cls._instance = super(SingletonMetaClass, cls).__call__(*args, **kwargs)  # 这里创建的是子类的实例对象，可以参考type的call方法推测
        return cls._instance


class TestCls(object):
    __metaclass__ = SingletonMetaClass

    # 先用 元类创建 TestCls 类对象，程序自动调用，不需要显示调用

    def __init__(self):
        print "haha"


class TestCls2(object):
    __metaclass__ = SingletonMetaClass

    # 当前类创建了实例对象的 时候，对象调用时才会发生
    def __call__(self, *args, **kwargs):
        print "9999999999999"


if __name__ == '__main__':
    # print TestCls()
    # print TestCls()

    print TestCls2._instance
    a = TestCls2()
    print TestCls2._instance
    b = TestCls2()
    # print a()
    # print b()
    print a
    print a == b

    print "--------------------------"
    # type 类的call 方法就是，创建 对应 类对象 的 实例对象
    kk = type("test11111", (), {}).__call__()
    print kk
    print object.__call__()

    # 总结 call 方法的用法， call方法是一个对象方法， 类对象实用时会创建  实例对象， 实例对象创建时: 根据类重写的不同，五花八门的都有
