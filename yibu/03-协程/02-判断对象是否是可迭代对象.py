from collections import Iterable  # 可迭代类型
from collections import Iterator  # 迭代器类型


# 判断对象是否是 类型 的实例对象 返回值为真或者假
# isinstance(对象, 类型)

print(isinstance(100, int))  # True 判断一个数据是否是整型类型
print(isinstance(100, str))  # False 判断一个数据是否是字符串类型

# 判断对象是否是可迭代类型
print(isinstance([1, 2, 3, 4], Iterable))  # True

# 判断对象是否是迭代器类型
data_iter = iter([1, 2, 3, 4])  # 取出可迭代对象中的迭代器

data2_iter = iter(data_iter)    # 迭代器是可迭代类型 通过iter(迭代器)取出迭代器还是原来的迭代器
print(id(data_iter), id(data2_iter))

print(isinstance(data_iter, Iterator))  # True
print(isinstance([1, 2, 3, 4], Iterator))  # False 可迭代对象不是迭代器
print(isinstance(data_iter, Iterable))  # True Python规定: 迭代器必须是可迭代类型对象

# 因为迭代器是可迭代对象 所以能够使用for循环进行遍历
for i in data_iter:
    print(i)