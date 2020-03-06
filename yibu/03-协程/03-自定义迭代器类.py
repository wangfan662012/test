class FibIter(object):
    """自定义迭代器类"""
    def __init__(self, count):
        self.number1 = 1
        self.number2 = 1
        self.cur = 0   # 计数器 表示当前次数
        self.count = count  # 总次数
    def __iter__(self):
        """和iter函数是对应起来 提供迭代器"""
        # print(" __iter__执行了")
        return self
    def __next__(self):
        """和next函数对应起来 提供下一个值"""
        # print("__next__执行了")
        if self.cur >= self.count:
            raise StopIteration  # 如果迭代完成就抛出异常
        else:
            ret = self.number1
            self.number1, self.number2 = self.number2, self.number1+self.number2
            self.cur += 1
            return ret

# 1 1 2 3 5 8 13 21 34
# 通过调用迭代器类 创建 迭代器对象
f = FibIter(10)
for i in f:
    print(i, end=" ")

# iter(f)
# str(对象)   ===>  对象.__str__()
# 迭代器 = iter(迭代器)  # 魔法方法 迭代器对象.__iter__()
# 下一个值 = next(迭代器)  # 魔法方法 迭代器对象.__next__()
# f只要是可迭代对象就可以  迭代器是可迭代类型 所以f可以是迭代器
