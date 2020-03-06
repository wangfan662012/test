import pandas as pd
import random
# 1. 读取数据
movie = pd.read_csv('test/case/players.csv')
# 2. 了解数据的基本信息
print(movie.head())
# 3. 获取导演列信息,并转成list
directors = movie['e'].to_list()
# 4. 去重后获取个数
num = set(directors)
print(type(num))
print(len(num))