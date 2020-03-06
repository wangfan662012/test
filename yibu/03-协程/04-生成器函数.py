def gen():
    """生成器函数"""
    print("in gen")
    yield 1000
    # 暂停当前代码执行将后面的值返回到调用生成器的地方;
    # 当生成器再次被调用<唤醒> 从上次暂停的位置继续往下执行
    yield 1024
    yield 2048

# 调用生成器函数 产生生成器对象  print(type(g))
# 生成器是迭代器 -> 可迭代对象
g = gen()
for i in g:
    print(i)
