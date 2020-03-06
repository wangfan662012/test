import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import pymysql

sql = 'select name,average_price from house_message limit 5;'
conn = pymysql.connect(host='192.168.159.128', port=3306, user='root', passwd='root', db='test_case', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
df = pd.read_sql(sql, con=conn)
print(df)
# df1 = np.array(df) #先使用array()将DataFrame转换一下
# df2 = df1.tolist()#再将转换后的数据用tolist()转成列表
name = np.array(df['name']).tolist()
price = np.array(df['average_price']).tolist()

# 绘制柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 第一个参数为柱的横坐标, 第二个参数为柱的高度, 参数align为柱的对齐方式
plt.bar(name, price, align='center')
# 设置横坐标的文字说明
plt.xlabel(u"楼盘")
# 设置纵坐标的文字说明
plt.ylabel(u"价格")
# 设置标题
plt.title(u"太原楼盘价格")
# 绘图
plt.show()


