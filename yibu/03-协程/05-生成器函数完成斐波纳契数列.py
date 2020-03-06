

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
        yield ret
    # 当生成器执行完成后 会自动抛出异常
    return 1001

# 调用生成器函数创建生成器对象

fg = Fibgen(1)

# for i in fg:
#     print(i)

print(next(fg))
# 在生成器中如果含return 不能直接获取结果 需要捕获异常 然后异常对象.values
try:
    print(next(fg))
except Exception as e:
    print("获取生成器中return 为:%d" % e.value)

# 1 1 2 3 5 8 13