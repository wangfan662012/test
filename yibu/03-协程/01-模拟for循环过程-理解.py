# 1 可迭代对象 第一个元素的位置放入迭代器中
# 2 用户通过迭代器取出 下一个元素 (当前位置对应的元素) next
# 3 迭代器自动指向   下一次即将被访问的元素
# 4 重复2 3 步直到迭代完成
# 可迭代对象角色:  提供数据 提供迭代器
# 迭代器角色:   记录访问位置  让用户可以间接访问数据
# for i in data:
#   print(i)   # for循环内部已经将异常捕获了

"""
# for循环的本质

遍历的是可迭代对象
for item in Iterable 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器，
然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item，
当遇到StopIteration的异常后循环结束。

遍历的是迭代器
for item in Iterator 循环的迭代器，不断调用next()方法来获取下一个值并将其赋值给item，
当遇到StopIteration的异常后循环结束。
"""
data = [1, 2, 3, 4, 5, 6]

# 1 获取到可迭代对象中提供的迭代器 返回值就是迭代器
data_iter = iter(data)
# print(data_iter, type(data_iter))

# 2 通过迭代器取出下一个元素  返回值就是下一个元素的值
#   如果已经没有元素可以取出了 就会抛出一个异常 StopIteration停止迭代
while True:
    try:
        i = next(data_iter)
    except StopIteration:
        break
    else:
        print(i)

