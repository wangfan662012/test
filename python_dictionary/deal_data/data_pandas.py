import numpy as np
import pandas as pd
import pandas_profiling

series = pd.Series([3, 4, 7, np.nan, 9, 8])
dates = pd.date_range('20191101', periods=6)
dataframe = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=['一', '二', '三', '四', 'A'])
df = pd.DataFrame(np.arange(30).reshape(6, 5), index=dates, columns=['A', 'B', 'C', 'D', 'E'])
df_1 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20180310'),
                    'C': pd.Series(1,index=list(range(4))),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", np.nan, np.nan]),
                    'F': 'foo'
                    })
print(dataframe)

# print(series)
# print(dataframe)
# print(dataframe['一'])
# print(dataframe.A)
# print(dataframe.dtypes)
# print(dataframe.index)
# print(dataframe.columns)
# print(dataframe.values)
# print(dataframe.describe())  #列表统计信息
# print(dataframe.T)  #列表翻转
# print(dataframe.sort_index(axis=0, ascending=False)) #axis等于1,列按正序排列, 等于0倒序, ascending=false行倒叙显示
# print(dataframe.sort_values(by='一'))  #按值进行排序
# print(dataframe[0:3], dataframe['20191101':'20191102']) #两次进行选择 第一次切片选择 第二次按照筛选条件进行选择
# print(dataframe.loc['20191101':'20191103', ['A', '一']])  # 按照行标签进行选择 精确选择
# print(dataframe.iloc[[3, 5], [1, 3]]) # 第3和5行的第1和3列,注意从0开始数
# print(dataframe.ix['20191101':'20191103', [1,3]]) #列名和行下标混合使用
# print(dataframe[dataframe.A >0]) #根据条件判断

# df.loc['20191103', 'B'] = 99
# df.iloc[4, 4] = 88
# df.A[df.A > 15] = 77
# df['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20191104', periods=6))  # 增加一列
# df = df.dropna(axis=0, how='any')  # 0对行进行操作 1对列进行操作 any:只要存在NaN即可drop掉 all:必须全部是NaN才可drop
# df = df.fillna(value=0)
# print(pd.isnull(df))
# print(df)

# data = pd.read_csv('detaillist.csv')  # 读取文件,csv、excel、json、html、pickle都可
# data.to_excel('detaillist.xlsx')   # 转换文件格式
# print(data)

# 合并数据
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['c','d','g','h'])
# axis = pd.concat([df1, df2], axis=0, ignore_index=True)  # axis=0表示竖项合并 1表示横项合并 ingnore_index重置序列
# print(axis)
# join = pd.concat([df2, df3], axis=1, join='outer')
# print(join)
# append = df1.append(df2, ignore_index=True)  # 将df2合并到df1的下面 并重置index
# print(append)

# pandas合并mrge
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'k2': ['K0', 'K1', 'K1', 'K1'],
                     'k3': ['K0', 'K0', 'K2', 'K0'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'k2': ['K0', 'K1', 'K2', 'K0'],
                      'k3': ['K1', 'K0', 'K1', 'K1'],
                      'C': ['C0', 'C1', 'C2',  'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# merge = pd.merge(left, right, on='key')
# print(merge)
# inner = pd.merge(left, right, on=['k2', 'k3'], how='inner')
# print(inner)
# outer = pd.merge(left, right, on=['k2', 'k3'], how='outer')
# print(outer)
# index = pd.merge(left, right, left_index=True, right_index=True, how='outer')  # 根据index索引进行合并 并选择外联合并
# print(index)


