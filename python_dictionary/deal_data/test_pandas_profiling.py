import matplotlib.pyplot as plt
import seaborn as sbn
import pandas_profiling as pdf
import pandas as pd
import datetime
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签

# 字符串类型时间段转换为整数秒
def change_date(d):
	h, m, s = map(int, d.split(":"))
	return datetime.timedelta(hours=h, minutes=m, seconds=s)

data = pd.read_csv('../case/detaillist.csv', converters={'time':change_date})
# 将纳秒转换为秒
data['time/s'] = data['time'] / np.timedelta64(1, 's')
# 数据整体描述
# print(data.describe())
# 数据前5行
print(data.head())
# 数据类型
print(data.dtypes)
# profile = data.profile_report(title='report')
# profile1 = pdf.ProfileReport(data, title='report')
# profile.to_file(output_file='report.html')



