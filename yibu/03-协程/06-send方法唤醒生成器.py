def Fibgen(count):
    """生成器函数  count是总次数"""
    number1 = 1
    number2 = 1
    cur = 0  # 当前次数
    while cur < count:
        ret = number1
        number1, number2 = number2, number1 + number2
        cur += 1  # 次数加1
        # 1 暂停 返回值给调用生成器地方; 2 将函数从暂停的位置继续往下执行
        data = yield ret
        print("在生成器中收到了数据 %s" % data)

# 创建生成器对象
f = Fibgen(10)

# 第一次执行生成器 必须用next 后面随意
print(f.send('今天天气还可以'))

# 驱动生成器往下执行一步  - 取出下一个值
print(next(f))

# .send方法 1 可以让生成器往下执行一步 - 取出下一个值
# 方法参数表示 给生成器代码传的数据 2 给生成器代码发送消息
print(f.send('今天天气还可以'))
print(next(f))


